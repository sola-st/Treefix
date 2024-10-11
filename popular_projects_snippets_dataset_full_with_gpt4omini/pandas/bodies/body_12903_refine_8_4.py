import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover
import numpy as np # pragma: no cover
import pandas.testing as tm # pragma: no cover

vals = np.random.rand(4, 2).tolist() # pragma: no cover
index_nm = 'Quarterly Periods' # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover
import pandas.testing as tm # pragma: no cover

vals = [[1, 'A'], [2, 'B'], [3, 'C'], [4, 'D']] # pragma: no cover
index_nm = 'Quarter' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
from l3.Runtime import _l_
df = DataFrame(
    vals,
    index=pd.Index(
        (pd.Period(f"2022Q{q}") for q in range(1, 5)), name=index_nm
    ),
)
_l_(3920)
out = df.to_json(orient="table")
_l_(3921)
result = pd.read_json(out, orient="table")
_l_(3922)
tm.assert_frame_equal(df, result)
_l_(3923)
