arr = [1,2,1,3,4,2,5,4,1,3]
paircount = 0

for x in arr:
  freq = arr.count(x)
  #print(x, freq)
  pairs = freq//2
  paircount += pairs
  arr = [y for y in arr if y != x]
print(paircount)
