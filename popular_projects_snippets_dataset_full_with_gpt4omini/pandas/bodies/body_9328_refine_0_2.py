import pandas as pd # pragma: no cover
import pyarrow as pa # pragma: no cover
import pandas.testing as tm # pragma: no cover

data = [[1, 2], [3, 4], [5, 6], [7, 8]] # pragma: no cover
pd = type('Mock', (object,), {'DataFrame': pd.DataFrame})() # pragma: no cover
pa = type('Mock', (object,), {'table': lambda df: pa.Table.from_pandas(df)})() # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': lambda df1, df2: None})() # pragma: no cover

import pandas as pd # pragma: no cover
import pyarrow as pa # pragma: no cover
import pandas.testing as tm # pragma: no cover

data = [[1, 2], [3, 4], [5, 6], [7, 8]] # pragma: no cover
df = pd.DataFrame(data) # pragma: no cover
pd = type('Mock', (object,), {'DataFrame': pd.DataFrame})() # pragma: no cover
pa = type('Mock', (object,), {'table': pa.Table})() # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': lambda df1, df2: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arrow_compat.py
# https://github.com/pandas-dev/pandas/issues/38525

from l3.Runtime import _l_
df = pd.DataFrame({"a": data})
_l_(4767)
table = pa.table(df)
_l_(4768)
result = table.slice(2, None).to_pandas()
_l_(4769)
expected = df.iloc[2:].reset_index(drop=True)
_l_(4770)
tm.assert_frame_equal(result, expected)
_l_(4771)

# no missing values
df2 = df.fillna(data[0])
_l_(4772)
table = pa.table(df2)
_l_(4773)
result = table.slice(2, None).to_pandas()
_l_(4774)
expected = df2.iloc[2:].reset_index(drop=True)
_l_(4775)
tm.assert_frame_equal(result, expected)
_l_(4776)
