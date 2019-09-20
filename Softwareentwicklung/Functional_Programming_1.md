# 1.

TODO: Order the list by the length of author name

```python
# Sorted by total length
sorted(authors, key=len)
# Sorted by first names length
sorted(authors, key=lambda s: len(s.split()[0]))
```

# 2.

TODO: Order the list alphabetically by last name

```python
sorted(authors, key=lambda s: s.split()[1])
```

# 3.

TODO: Rewrite this code to keep map, but get rid of the anonymous lambda function (use a regular function instead).

```python
def mult(x):
    return x*2

list(map(mult,val))
```

# 4.

TODO: Rewrite this code to get rid of the anonymous lambda function.


```python
def filt(x):
    l = []
    for i in x:
        if (i % 2 != 0 and i > 1):
            l.append(i)
    return l

filt(val)
```

# 5.

Actually, this special case of reduce is so frequent that Python provides a dedicated function for that. Which one?

```python
sum(val)
```

# 6.

TODO: Rewrite this code to get rid of the anonymous lambda function.

```python
def multiply(x):  
    product = 1
    for i in x:
        product *= i  
    return product  

multiply(val)
```
# 7.

TODO: Get rid of the lambda function in the previous example using operator.mul.

```python
import operator
reduce(operator.mul, val)
