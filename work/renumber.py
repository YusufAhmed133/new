import re,sys
p=sys.argv[1]; s=open(p).read()
body,_,rest=s.partition('\nWord count:')
countline,_,foots=('Word count:'+rest).partition('\n\n')
defs=dict(re.findall(r'^\[\^(\d+)\]: (.*)$',foots,flags=re.M))
order=[]
for m in re.finditer(r'\[\^(\d+)\]',body):
    if m.group(1) not in order: order.append(m.group(1))
mp={old:str(i+1) for i,old in enumerate(order)}
body=re.sub(r'\[\^(\d+)\]',lambda m:'[^'+mp[m.group(1)]+']',body)
newdefs=[]
for old in order:
    t=defs[old]
    t=re.sub(r'\(n (\d+)\)',lambda m:'(n '+mp.get(m.group(1),'??'+m.group(1))+')',t)
    newdefs.append(f'[^{mp[old]}]: {t}')
open(p,'w').write(body+'\n'+countline+'\n\n'+'\n'.join(newdefs)+'\n')
print('footnotes',len(order), 'unmapped refs' if '??' in ''.join(newdefs) else 'ok')
