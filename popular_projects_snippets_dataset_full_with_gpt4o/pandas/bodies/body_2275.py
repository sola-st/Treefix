# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_alter_axes.py
# GH 6785
# set the index manually

from l3.Runtime import _l_
df = DataFrame([{"ts": datetime(2014, 4, 1, tzinfo=pytz.utc), "foo": 1}])
_l_(21343)
expected = df.set_index("ts")
_l_(21344)
df.index = df["ts"]
_l_(21345)
df.pop("ts")
_l_(21346)
tm.assert_frame_equal(df, expected)
_l_(21347)
