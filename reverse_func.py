m= [[1, 2], [3, 4], [5, 6, 7]]

def reverse_func():
  newList=[]
  m.reverse()
  for l in m:
    l.reverse()
    newList.append(l)
  print(newList)
reverse_func()