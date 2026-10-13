#!/usr/bin/env python3
"""Build the submission .docx from ANSWER.md: italicise case names (body and footnotes), bold party headings, TNR 12 double spaced, page numbers, Word footnotes."""
import re, subprocess, sys
src=sys.argv[1]; out=sys.argv[2]
s=open(src,encoding='utf-8').read()
CASES=[
 'Gibson v Manchester City Council','Empirnall Holdings Pty Ltd v Machon Paull Partners Pty Ltd',
 'Australian Woollen Mills Pty Ltd v Commonwealth','Ermogenous v Greek Orthodox Community of SA Inc',
 'Masters v Cameron','Godecke v Kirwan','Meehan v Jones','Placer Development Ltd v Commonwealth',
 'Trident General Insurance Co Ltd v McNiece Bros Pty Ltd','Coulls v Bagot’s Executor and Trustee Co Ltd','Coulls v Bagot’s Executor & Trustee Co Ltd','Wilson v Darling Island Stevedoring & Lighterage Co Ltd',
 'Brambles Holdings Ltd v Bathurst City Council','Integrated Computer Services Pty Ltd v Digital Equipment Corp (Aust) Pty Ltd',
 'Eccles v Bryant and Pollock','Eccles v Bryant','TA Sundell & Sons Pty Ltd v Emm Yannoulatos (Overseas) Pty Ltd','Wigan v Edwards',
 'Pao On v Lau Yiu Long','Banque Brussels Lambert SA v Australian National Industries Ltd',
 'Council of the Upper Hunter County District v Australian Chilling and Freezing Co Ltd','G Scammell and Nephew Ltd v Ouston',
 'Roscorla v Thomas','Beaton v McDivitt','Secured Income Real Estate (Aust) Ltd v St Martins Investments Pty Ltd',
 'Thorby v Goldberg','Biotechnology Australia Pty Ltd v Pace','Winn v Bull','Port Jackson Stevedoring Pty Ltd v Salmond & Spraggon (Aust) Pty Ltd',
]
SHORT=['Beaton','Gibson','Empirnall','Australian Woollen Mills','Ermogenous','Masters','Godecke','Meehan','Placer','Trident','Coulls','Brambles','Pao On','Banque Brussels','Upper Hunter','Sundell']
body,_,rest=s.partition('\n[^1]:')
foot='[^1]:'+rest
def ital(text, names):
    pat=re.compile('|'.join(r'(?<![\w])'+re.escape(n)+r'(?![\w])' for n in sorted(names,key=len,reverse=True)))
    return pat.sub(lambda m:'*'+m.group(0)+'*', text)
# footnotes: full names and short titles (also inside the ('Short') parentheses)
foot=ital(foot, CASES+SHORT)
# body: short titles only where used as case names (not 'Mrs Coulls')
body=ital(body, [x for x in SHORT if x!='Coulls'])
body=re.sub(r'^(I{1,3}\. [A-Z][A-Z v()]+)$', r'**\1**', body, flags=re.M)
md=body+'\n[^1]:'+foot[5:]
open('build_tmp.md','w',encoding='utf-8').write(md)
subprocess.run(['pandoc','build_tmp.md','-f','markdown-smart','-o',out,'--reference-doc','reference.docx'],check=True)
print('built',out)
