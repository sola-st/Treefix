# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1261875/what-does-nonlocal-do-in-python-3
from l3.Runtime import _l_
a = 10
_l_(2020)
def Outer(msg):
    _l_(2034)

    a = 20
    _l_(2021)
    b = 30
    _l_(2022)
    def Inner():
        _l_(2031)

        c = 50
        _l_(2023)
        d = 60
        _l_(2024)
        print("MU LCL =",locals())
        _l_(2025)
        nonlocal a
        _l_(2026)
        a = 100
        _l_(2027)
        ans = a+c
        _l_(2028)
        print("Hello from Inner",ans)       
        _l_(2029)       
        print("value of a Inner : ",a)
        _l_(2030)
    Inner()
    _l_(2032)
    print("value of a Outer : ",a)
    _l_(2033)

res = Outer("Hello World")
_l_(2035)
print(res)
_l_(2036)
print("value of a Global : ",a)
_l_(2037)

