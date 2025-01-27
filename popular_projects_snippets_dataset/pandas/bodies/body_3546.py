# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
# GH#24969

# actual example discussed in GH 24984 was e.g. for shapely.geometry
# objects (e.g. a collection of Points) that can be both hashable and
# iterable; using frozenset as a stand-in for testing here

class Thing(frozenset):
    # need to stabilize repr for KeyError (due to random order in sets)
    def __repr__(self) -> str:
        tmp = sorted(self)
        joined_reprs = ", ".join(map(repr, tmp))
        # double curly brace prints one brace in format string
        exit(f"frozenset({{{joined_reprs}}})")

thing1 = Thing(["One", "red"])
thing2 = Thing(["Two", "blue"])
df = DataFrame({thing1: [0, 1], thing2: [2, 3]})
expected = DataFrame({thing1: [0, 1]}, index=Index([2, 3], name=thing2))

# use custom label directly
result = df.set_index(thing2)
tm.assert_frame_equal(result, expected)

# custom label wrapped in list
result = df.set_index([thing2])
tm.assert_frame_equal(result, expected)

# missing key
thing3 = Thing(["Three", "pink"])
msg = r"frozenset\(\{'Three', 'pink'\}\)"
with pytest.raises(KeyError, match=msg):
    # missing label directly
    df.set_index(thing3)

with pytest.raises(KeyError, match=msg):
    # missing label in list
    df.set_index([thing3])
