n,m,k = map(int, input().split())
data = list(map(int, input().split()))
count = 0;

data.sort(reverse=True)
first = data[0]
second = data[1]

print(first, second)
while(True):
  for i in range(k):
    if m == 0:
      break
    count += first
    m -= 1
  if m == 0:
    break
  count += second
  m-=1


print(count)