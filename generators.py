"""generators are iterators you can only iterate over once"""

def gen_func():
    for x in range(10):
        yield x

for i in gen_func():
    print(i)


# generator used to calculate fibonacci
def fibonacci(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibonacci(10):
    print(x)
