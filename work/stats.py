import re,sys
s=open(sys.argv[1]).read()
body=re.sub(r'\[\^\d+\]','',s.split('Word count:')[0])
words=body.split(); n=len(words)
q=re.findall(r"‘(.+?)’(?![a-z])",body,flags=re.S)
qw=sum(len(x.split()) for x in q)
flat=' '.join(body.split())
ss=[x for x in re.split(r'(?<=[.])\s+(?=[A-Z‘])',flat) if len(x.split())>2 and not re.match(r'^I+\.',x)]
L=[len(x.split()) for x in ss]
semi=flat.count(';'); colon=flat.count(':')
withmark=sum(1 for x in ss if ';' in x or ':' in x)
print(f'body {n} stated {n+3} | quoted {qw} ({100*qw/n:.1f}%) | sentences {len(L)} mean {sum(L)/len(L):.1f} | under12 {100*sum(1 for l in L if l<12)/len(L):.1f}% | >45 {[l for l in L if l>45]} | semi/100 {100*semi/n:.2f} colon/100 {100*colon/n:.2f} | sent w/ ;: {100*withmark/len(L):.1f}%')
