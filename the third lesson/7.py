"# -- coding: utf-8 --"
n = int(input())
pf= 1
ps = 0
for i in range(1, n + 1):
    pf *= i
    ps += pf
print(ps)