#!/usr/bin/env python3
"""Verify quotations in a draft against the casebook text (14th ed chapters, W1 casebook, Pao On extract, problem).
Usage: python3 -I verify.py draft.md
Reports, for each quoted span: FOUND/NOT FOUND, source, printed casebook page, and the nearest preceding report-page marker [nnn]."""
import re, sys, unicodedata, glob
BASE='/home/user/new/drive'
SRC={}
for f in sorted(glob.glob(BASE+'/casebook/CB14_ch*.txt')):
    SRC[f.split('/')[-1]]=open(f,encoding='utf-8').read()
for f,n in [('/txt/W1L1_casebook.txt','W1L1'),('/txt/W1L2_casebook.txt','W1L2'),('/txt/ACTUAL TASKKK.txt','PROBLEM')]:
    SRC[n]=open(BASE+f,encoding='utf-8').read()
import subprocess
SRC['PAOON_EXTRACT']=subprocess.run(['pdftotext','-layout',BASE+'/readings/W2 L1 - Consideration_ Part 1/Extract from Pao On v Lau Yiu Long 1980 Privy Council.pdf','-'],capture_output=True,text=True).stdout
def norm(s):
    s=unicodedata.normalize('NFKC',s).replace('​','').replace('­','')
    s=s.replace('‘',"'").replace('’',"'").replace('“','"').replace('”','"').replace('–','-').replace('—','-')
    s=s.replace('ﬁ','fi').replace('ﬀ','ff').replace('ﬂ','fl')
    return s
# build normalised stream with position map to page and report markers
INDEX={}
for name,t in SRC.items():
    t=norm(t)
    out=[];meta=[];page='?';rep='?'
    lines=t.split('\n')
    for ln in lines:
        m=re.match(r'===== PDF \d+ \| expected printed p (\d+)',ln)
        if m: page=m.group(1); continue
        if re.match(r'^\s*(Part [IVX]+:|.*Chapter \d+\s*$)',ln): continue
        if re.search(r'\[\d+\.\d+\]\s+\d+\s*$|^\s*\d+\s+\[\d+\.\d+\]\s*$',ln): continue
        if re.search(r'\bcont\.\s*$',ln): continue
        # strip report markers from text but record them
        pieces=re.split(r'(\[\d{2,4}\])',ln)
        for p in pieces:
            mm=re.fullmatch(r'\[(\d{2,4})\]',p)
            if mm and not (len(mm.group(1))==4 and 1500<=int(mm.group(1))<=2100):
                rep=mm.group(1); continue
            for ch in p+' ':
                out.append(ch); meta.append((page,rep))
    s=''.join(out)
    # de-hyphenate line-break hyphens and collapse spaces, keep map
    s2=[];m2=[];i=0
    while i<len(s):
        ch=s[i]
        if ch=='-' and i+1<len(s) and s[i+1]==' ' and i>0 and s[i-1].isalpha():
            j=i+1
            while j<len(s) and s[j]==' ': j+=1
            if j<len(s) and s[j].islower():
                i=j; continue
        if ch.isspace():
            if s2 and s2[-1]==' ': i+=1; continue
            ch=' '
        s2.append(ch); m2.append(meta[i]); i+=1
    INDEX[name]=(''.join(s2),m2)
def find(q):
    qn=re.sub(r'\s+',' ',norm(q)).strip()
    parts=[p.strip() for p in re.split(r'\s*(?:…|\.\.\.)\s*',qn) if p.strip()]
    res=[]
    for name,(s,m) in INDEX.items():
        ok=True;pos=0;hits=[]
        for p in parts:
            p2=re.sub(r'\[[^\]]*\]','',p).strip() if '[' in p else p
            k=s.find(p,pos) if p in s else -1
            if k<0:
                # allow bracketed alterations: match segments around brackets
                segs=[x.strip() for x in re.split(r'\[[^\]]*\]',p) if x.strip()]
                kk=pos;seg_ok=True;first=None
                for sg in segs:
                    k2=s.find(sg,kk)
                    if k2<0: seg_ok=False;break
                    if first is None: first=k2
                    kk=k2+len(sg)
                if not seg_ok: ok=False;break
                hits.append((first,kk));pos=kk
            else:
                hits.append((k,k+len(p)));pos=k+len(p)
        if ok and hits:
            a=hits[0][0];b=hits[-1][1]-1
            res.append((name,m[a][0],m[b][0],m[a][1],m[b][1]))
    return res
if __name__=='__main__':
    txt=open(sys.argv[1],encoding='utf-8').read()
    body=txt
    qs=re.findall(r"(?<![A-Za-z])‘(.+?)’(?![A-Za-z])",body,flags=re.S)
    bad=0
    for q in qs:
        if len(q.split())<2: continue
        r=find(q)
        if not r:
            bad+=1;print('NOT FOUND :',q)
        else:
            srcs='; '.join(f"{n} p{a}{'-'+b if b!=a else ''} rep[{ra}{'-'+rb if rb!=ra else ''}]" for n,a,b,ra,rb in r[:3])
            print('FOUND     :',q[:70],'=>',srcs)
    print('TOTAL',len(qs),'NOT FOUND',bad)
