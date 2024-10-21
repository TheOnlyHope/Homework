import math

a = 0
n = 1000000
sum = 0
nøyaktighet = 0.000001

def f(x):
    return(100/(1 + (2 * (math.e**((-0.05)*x)))))

count = 1

while sum <= 9999:
    sum = sum + f(a + (count+0.5)*nøyaktighet) * nøyaktighet
    count += 1

b = count * nøyaktighet
n = 1000000
delta_x = (b - a)/n
sum = 0

def f(x):
    return(100/(1 + (2 * (math.e**((-0.05)*x)))))

for i in range(n):
    sum = sum + f(a + (i+0.5)*delta_x) * delta_x

print(round(sum, 20))

print(count * nøyaktighet)
