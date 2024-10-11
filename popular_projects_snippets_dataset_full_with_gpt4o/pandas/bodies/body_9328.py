# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arrow_compat.py
# https://github.com/pandas-dev/pandas/issues/38525

from l3.Runtime import _l_
df = pd.DataFrame({"a": data})
_l_(16029)
table = pa.table(df)
_l_(16030)
result = table.slice(2, None).to_pandas()
_l_(16031)
expected = df.iloc[2:].reset_index(drop=True)
_l_(16032)
tm.assert_frame_equal(result, expected)
_l_(16033)

# no missing values
df2 = df.fillna(data[0])
_l_(16034)
table = pa.table(df2)
_l_(16035)
result = table.slice(2, None).to_pandas()
_l_(16036)
expected = df2.iloc[2:].reset_index(drop=True)
_l_(16037)
tm.assert_frame_equal(result, expected)
_l_(16038)
