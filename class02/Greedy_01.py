n = int(input())
lost = map(int, input().split())
more = map(int, input().split())
d=[1] * (n+2) # [1,1,1,1,1,1,1,1,1,1,1,1]
# 10 = [1,1,1,1,1,1,1,1,1,1]
#1 3 5 7 8  lost
#7 5 2 9 6 more 2 
count =0

for i in lost:
  d[i] -= 1
# lost의 인덱스 뺴기 1을 해준다 =[1,0,1,0,1,0,1,0,0,1,1,1]
for i in more:
  d[i] += 1
# more 은 여분의 체육복을 가져운 온 학생들 = [1,0,2,0,1,1,2,1,0,2,1,1]

for i in range(1, n+1): # range(1,11)
  if d[i -1] == 0 and d[i] == 2:
  # d[2-1] == 0 and d[2]==2
    d[i-1:i+1] =[1,1]
  # d[1:3] = [1,1]  =>    [1,1,1,0,1,1,2,1,0,2,1,1]
  elif d[i]==0 and d[i+1] == 2:
  # d[8] == 0 and d[9] == 2
    d[i:i+2] =[1,1]
  # d[8:10] = [1,1] =>  [1,1,1,0,1,1,2,1,1,1,1,1]

print(d)

answer = len([x for x in d[1:-1] if x > 0])
print(answer)