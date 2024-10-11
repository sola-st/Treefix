import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': ['...', '...'], 'D': [5, 6]}) # pragma: no cover
np.array = lambda x: np.ndarray(buffer=np.array(list(x)).data, shape=(len(x),), dtype=object) # pragma: no cover
np.where = lambda condition: (np.argwhere(condition),) # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': ['...', '...'], 'D': [5, 6]}) # pragma: no cover
np.array = lambda x: np.ndarray(shape=(len(x),), dtype=object, buffer=np.array(list(x), dtype=object)) # pragma: no cover
np.where = lambda condition: (np.nonzero(condition)[0],) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
from l3.Runtime import _l_
try:
    _l_(18205)

    fst_line = np.array(repr(df).splitlines()[0].split())
    _l_(18201)
    cand_col = np.where(fst_line == "...")[0][0]
    _l_(18202)
except IndexError:
    _l_(18204)

    aux = False
    _l_(18203)
    exit(aux)
# Make sure each row has this ... in the same place
r = repr(df)
_l_(18206)
for ix, _ in enumerate(r.splitlines()):
    _l_(18209)

    if not r.split()[cand_col] == "...":
        _l_(18208)

        aux = False
        _l_(18207)
        exit(aux)
aux = True
_l_(18210)
exit(aux)
