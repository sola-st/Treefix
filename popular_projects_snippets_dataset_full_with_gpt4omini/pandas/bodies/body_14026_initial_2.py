import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

df = pd.DataFrame({'column1': ['...', '...', '...'], 'column2': [1, 2, 3]}) # pragma: no cover
np = type('Mock', (object,), {'array': np.array, 'where': np.where}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
from l3.Runtime import _l_
try:
    _l_(6222)

    fst_line = np.array(repr(df).splitlines()[0].split())
    _l_(6218)
    cand_col = np.where(fst_line == "...")[0][0]
    _l_(6219)
except IndexError:
    _l_(6221)

    aux = False
    _l_(6220)
    exit(aux)
# Make sure each row has this ... in the same place
r = repr(df)
_l_(6223)
for ix, _ in enumerate(r.splitlines()):
    _l_(6226)

    if not r.split()[cand_col] == "...":
        _l_(6225)

        aux = False
        _l_(6224)
        exit(aux)
aux = True
_l_(6227)
exit(aux)
