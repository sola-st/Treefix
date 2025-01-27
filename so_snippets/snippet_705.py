# Extracted from https://stackoverflow.com/questions/334655/passing-a-dictionary-to-a-function-as-keyword-parameters
In[1]: def myfunc(a=1, b=2):
In[2]:    print(a, b)

In[3]: mydict = {'a': 100, 'b': 200}

In[4]: myfunc(**mydict)
100 200

In[5]: mydict = {'a': 100}
In[6]: myfunc(**mydict)
100 2

In[7]: mydict = {'a': 100, 'b': 200}
In[8]: myfunc(a=3, **mydict)

TypeError: myfunc() got multiple values for keyword argument 'a'

In[9]:  mydict = {'a': 100, 'b': 200, 'c': 300}
In[10]: myfunc(**mydict)

TypeError: myfunc() got an unexpected keyword argument 'c'

In[11]: def myfunc2(a=None, **_):
In[12]:    print(a)

In[13]: mydict = {'a': 100, 'b': 200, 'c': 300}

In[14]: myfunc2(**mydict)
100

In[15]: import inspect
In[16]: mydict = {'a': 100, 'b': 200, 'c': 300}
In[17]: filtered_mydict = {k: v for k, v in mydict.items() if k in [p.name for p in inspect.signature(myfunc).parameters.values()]}
In[18]: myfunc(**filtered_mydict)
100 200

In[19]: def myfunc3(a, *posargs, b=2, **kwargs):
In[20]:    print(a, b)
In[21]:    print(posargs)
In[22]:    print(kwargs)

In[23]: mylist = [10, 20, 30]
In[24]: mydict = {'b': 200, 'c': 300}

In[25]: myfunc3(*mylist, **mydict)
10 200
(20, 30)
{'c': 300}

