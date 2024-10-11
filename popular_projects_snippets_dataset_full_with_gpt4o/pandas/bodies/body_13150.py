# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# cross-compat with differing reading/writing engines
from l3.Runtime import _l_
df = df_cross_compat
_l_(21992)
with tm.ensure_clean() as path:
    _l_(21999)

    df.to_parquet(path, engine=fp, compression=None)
    _l_(21993)

    with catch_warnings(record=True):
        _l_(21998)

        result = read_parquet(path, engine=pa)
        _l_(21994)
        tm.assert_frame_equal(result, df)
        _l_(21995)

        result = read_parquet(path, engine=pa, columns=["a", "d"])
        _l_(21996)
        tm.assert_frame_equal(result, df[["a", "d"]])
        _l_(21997)
