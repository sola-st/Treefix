# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1233448/no-multiline-lambda-in-python-why-not
#%%
from l3.Runtime import _l_
x = 1
_l_(14007)
y = 2
_l_(14008)

q = list(map(lambda t: (
    tx := t*x,
    ty := t*y,
    tx+ty
)[-1], [1, 2, 3]))
_l_(14009)

print(q)
_l_(14010)

