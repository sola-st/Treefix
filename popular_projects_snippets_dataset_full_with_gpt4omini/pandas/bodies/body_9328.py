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
