n=int(input())
vd=[0,1,2,5,6,8,9]
vd1=vd.copy()
c=0
i=1
while(i>0):
  d=[int(x) for x in str(i)]
  vd.extend(d)
  if(set(vd)== set(vd1)):
      c+=1
      if(c==n):
          print(int("".join(list(map(str,d)))))
          break
  i+=1
  vd=[0,1,2,5,6,8,9]
