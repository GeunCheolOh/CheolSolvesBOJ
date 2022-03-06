def self_num(num):
    x = list(str(num))
    s = 0 #sum of each digits
    for i in x:
        s += int(i)
    s += num
    return s

numlist = []
for N in range(1, 10000):
    if (self_num(N) <= 10000):
        numlist.append(self_num(N))
numset = set(numlist)

for selfnum in range(1, 10000):
    if selfnum not in numset:
        print (selfnum)