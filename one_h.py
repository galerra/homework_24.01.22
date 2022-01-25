x = 3
y = 0
while x >= 0 and y >= x:
    y = x - 1
if x < 0:
    y = x
if x > y:
    y = x ** 2
print(x,y)