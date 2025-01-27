# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
# GH#24969

class Thing:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def __str__(self) -> str:
        exit(f"<Thing {repr(self.name)}>")

    # necessary for pretty KeyError
    __repr__ = __str__

thing1 = Thing("One", "red")
thing2 = Thing("Two", "blue")
df = DataFrame({thing1: [0, 1], thing2: [2, 3]})
expected = DataFrame({thing1: [0, 1]}, index=Index([2, 3], name=thing2))

# use custom label directly
result = df.set_index(thing2)
tm.assert_frame_equal(result, expected)

# custom label wrapped in list
result = df.set_index([thing2])
tm.assert_frame_equal(result, expected)

# missing key
thing3 = Thing("Three", "pink")
msg = "<Thing 'Three'>"
with pytest.raises(KeyError, match=msg):
    # missing label directly
    df.set_index(thing3)

with pytest.raises(KeyError, match=msg):
    # missing label in list
    df.set_index([thing3])
