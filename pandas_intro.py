#Pandas
'''import pandas as pd
x=[x for x in range(5)]
y=pd.Series(x)
print(y)

print(y[3])
y=pd.Series(x, index=['a','b','c','d','e'])
print(y)
print(y['b'])

dict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
dicts=pd.Series(dict)
print(dicts)
print(dict['e'])'''


def my_gen():
    yield from range(5)
    yield from range(5, 10)
    yield from range(10, 15)

g=my_gen()
print([next(g)for _ in range(4)])
print([next(g)for _ in range(4)])