# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py
# more chunksize in append tests
from l3.Runtime import _l_
df = tm.makeDataFrame()
_l_(10428)
df["string"] = "foo"
_l_(10429)
df["float322"] = 1.0
_l_(10430)
df["float322"] = df["float322"].astype("float32")
_l_(10431)
df["bool"] = df["float322"] > 0
_l_(10432)
df["time1"] = Timestamp("20130101")
_l_(10433)
df["time2"] = Timestamp("20130102")
_l_(10434)
with ensure_clean_store(setup_path, mode="w") as store:
    _l_(10438)

    store.append("obj", df, chunksize=chunksize)
    _l_(10435)
    result = store.select("obj")
    _l_(10436)
    tm.assert_frame_equal(result, df)
    _l_(10437)
