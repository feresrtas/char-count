#Girilen string teki rakam ve harflerin sayısını veren program
s=input('enter string')
l=d=0
for c in s:
  if c.isdigit():d+=1 
  elif c.isalpha():l+=1
  else:pass
print('no of letters:',l)
print('no of digits:',d)