# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use
# Python list with append()
from l3.Runtime import _l_
np.mean(timeit.repeat(setup="a = []", stmt="a.append(1.0)", number=1000, repeat=5000)) * 1000
_l_(12021)
# 0.054 +/- 0.025 msec

# Python array with append()
np.mean(timeit.repeat(setup="import array; a = array.array('f')", stmt="a.append(1.0)", number=1000, repeat=5000)) * 1000
_l_(12022)
# 0.104 +/- 0.025 msec

# Numpy array with append()
np.mean(timeit.repeat(setup="import numpy as np; a = np.array([])", stmt="np.append(a, [1.0])", number=1000, repeat=5000)) * 1000
_l_(12023)
# 5.183 +/- 0.950 msec

# Python list using +=
np.mean(timeit.repeat(setup="a = []", stmt="a += [1.0]", number=1000, repeat=5000)) * 1000
_l_(12024)
# 0.062 +/- 0.021 msec

# Python array using += 
np.mean(timeit.repeat(setup="import array; a = array.array('f')", stmt="a += array.array('f', [1.0]) ", number=1000, repeat=5000)) * 1000
_l_(12025)
# 0.289 +/- 0.043 msec

# Python list using extend()
np.mean(timeit.repeat(setup="a = []", stmt="a.extend([1.0])", number=1000, repeat=5000)) * 1000
_l_(12026)
# 0.083 +/- 0.020 msec

# Python array using extend()
np.mean(timeit.repeat(setup="import array; a = array.array('f')", stmt="a.extend([1.0]) ", number=1000, repeat=5000)) * 1000
_l_(12027)
# 0.169 +/- 0.034

