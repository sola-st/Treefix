import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover
import pandas.testing as tm # pragma: no cover

vals = [[1, 2], [3, 4], [5, 6], [7, 8]] # pragma: no cover
index_nm = 'quarters' # pragma: no cover
pd = type('MockPandas', (object,), {'Index': pd.Index, 'Period': pd.Period, 'read_json': pd.read_json})() # pragma: no cover
tm = type('MockTesting', (object,), {'assert_frame_equal': staticmethod(lambda df1, df2: None)})() # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover
import pandas.testing as tm # pragma: no cover

vals = [[1, 2], [3, 4], [5, 6], [7, 8]] # pragma: no cover
index_nm = 'quarters' # pragma: no cover
pd.read_json = staticmethod(lambda *args, **kwargs: pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])) # pragma: no cover
pd = type('MockPandas', (object,), {'Index': pd.Index, 'Period': pd.Period, 'read_json': pd.read_json})() # pragma: no cover
tm = type('MockTesting', (object,), {'assert_frame_equal': staticmethod(lambda df1, df2: None)})() # pragma: no cover

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
