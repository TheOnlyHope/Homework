a = 0
b = 1
n = 1000000000
delta_x = (b - a)/n
sum = 0

def f(x):
    return(4/(1 + x**2))

for i in range(n):
    sum = sum + f(a + (i+0.5)*delta_x) * delta_x

print(round(sum, 20))
