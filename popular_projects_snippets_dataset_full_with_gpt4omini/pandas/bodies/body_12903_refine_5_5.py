import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover
import pandas.testing as tm # pragma: no cover

vals = [[1, 2], [3, 4], [5, 6], [7, 8]] # pragma: no cover
index_nm = 'quarter' # pragma: no cover
pd = type('Mock', (object,), {'Index': pd.Index, 'Period': pd.Period, 'read_json': pd.read_json})() # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': tm.assert_frame_equal})() # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover
import pandas.testing as tm # pragma: no cover

vals = [[1, 2], [3, 4], [5, 6], [7, 8]] # pragma: no cover
index_nm = 'quarter' # pragma: no cover
class MockPandas(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def Index(data, name): # pragma: no cover
        return pd.Index(data, name=name) # pragma: no cover
    @staticmethod # pragma: no cover
    def Period(freq): # pragma: no cover
        return pd.Period(freq) # pragma: no cover
    @staticmethod # pragma: no cover
    def read_json(data, orient=None): # pragma: no cover
        return pd.read_json(data, orient=orient) # pragma: no cover
pd = MockPandas() # pragma: no cover
class MockTesting(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_frame_equal(df1, df2): # pragma: no cover
        return df1.equals(df2) # pragma: no cover
tm = MockTesting() # pragma: no cover

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
