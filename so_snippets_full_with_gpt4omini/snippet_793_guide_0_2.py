import matplotlib.pyplot as plt # pragma: no cover

y = [2.56422, 3.77284, 3.52623, 3.51468, 3.02199] # pragma: no cover
z = [0.15, 0.3, 0.45, 0.6, 0.75] # pragma: no cover
n = [58, 651, 393, 203, 123] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14432557/scatter-plot-with-different-text-at-each-data-point
from l3.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(2931)

except ImportError:
    pass
y = [2.56422, 3.77284, 3.52623, 3.51468, 3.02199]
_l_(2932)
z = [0.15, 0.3, 0.45, 0.6, 0.75]
_l_(2933)
n = [58, 651, 393, 203, 123]
_l_(2934)

fig, ax = plt.scatter(z, y)
_l_(2935)

for i, txt in enumerate(n):
    _l_(2937)

    ax.annotate(txt, (z[i], y[i]))
    _l_(2936)
try:
    import matplotlib.pyplot as plt
    _l_(2939)

except ImportError:
    pass
plt.scatter(z, y)
_l_(2940)

for i, txt in enumerate(n):
    _l_(2942)

    plt.annotate(txt, (z[i], y[i]))
    _l_(2941)

