plt = type('Mock', (object,), {'plot': lambda x, y, z: None, 'legend': lambda x, y: None, 'show': lambda: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-simplest-manner-possible
from l3.Runtime import _l_
first = [1, 2, 4, 5, 4]
_l_(1956)
second = [3, 4, 2, 2, 3]
_l_(1957)
plt.plot(first, 'g--', second, 'r--')
_l_(1958)
plt.legend(['First List', 'Second List'], loc='upper left')
_l_(1959)
plt.show()
_l_(1960)

