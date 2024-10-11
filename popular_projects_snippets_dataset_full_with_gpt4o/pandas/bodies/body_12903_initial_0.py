import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover
import numpy as np # pragma: no cover

vals = np.random.rand(4, 3) # pragma: no cover
index_nm = 'quarter' # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': staticmethod(lambda x, y: None)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
from l3.Runtime import _l_
df = DataFrame(
    vals,
    index=pd.Index(
        (pd.Period(f"2022Q{q}") for q in range(1, 5)), name=index_nm
    ),
)
_l_(15494)
out = df.to_json(orient="table")
_l_(15495)
result = pd.read_json(out, orient="table")
_l_(15496)
tm.assert_frame_equal(df, result)
_l_(15497)
