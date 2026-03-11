
from __future__ import print_function
n = 4
for i in range(0, n):
    print(i)
li = ["geeks", "for", "geeks"]
for x in li:
    print(x)
    
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)

d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
for x in set1:
    print(x),
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
    
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)

for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)