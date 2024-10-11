# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1233448/no-multiline-lambda-in-python-why-not
#%%
from l3.Runtime import _l_
x = 1
_l_(1910)
y = 2
_l_(1911)

q = list(map(lambda t: (
    tx := t*x,
    ty := t*y,
    tx+ty
)[-1], [1, 2, 3]))
_l_(1912)

print(q)
_l_(1913)

