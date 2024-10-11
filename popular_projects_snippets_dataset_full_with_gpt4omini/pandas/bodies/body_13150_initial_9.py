tm = type('Mock', (object,), {'ensure_clean': staticmethod(lambda: open('temp.parquet', 'wb')), 'assert_frame_equal': staticmethod(lambda a, b: None)})() # pragma: no cover
fp = 'pyarrow' # pragma: no cover
read_parquet = lambda path, engine, columns=None: pd.read_parquet(path, engine=engine, columns=columns) # pragma: no cover
pa = 'pyarrow' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# cross-compat with differing reading/writing engines
from l3.Runtime import _l_
df = df_cross_compat
_l_(10608)
with tm.ensure_clean() as path:
    _l_(10615)

    df.to_parquet(path, engine=fp, compression=None)
    _l_(10609)

    with catch_warnings(record=True):
        _l_(10614)

        result = read_parquet(path, engine=pa)
        _l_(10610)
        tm.assert_frame_equal(result, df)
        _l_(10611)

        result = read_parquet(path, engine=pa, columns=["a", "d"])
        _l_(10612)
        tm.assert_frame_equal(result, df[["a", "d"]])
        _l_(10613)
