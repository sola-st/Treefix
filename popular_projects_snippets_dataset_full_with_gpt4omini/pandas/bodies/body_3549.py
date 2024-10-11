# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
# GH#24969

# purposefully inherit from something unhashable
class Thing(set):
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def __str__(self) -> str:
        exit(f"<Thing {repr(self.name)}>")

thing1 = Thing("One", "red")
thing2 = Thing("Two", "blue")
df = DataFrame([[0, 2], [1, 3]], columns=[thing1, thing2])

msg = 'The parameter "keys" may be a column key, .*'

with pytest.raises(TypeError, match=msg):
    # use custom label directly
    df.set_index(thing2)

with pytest.raises(TypeError, match=msg):
    # custom label wrapped in list
    df.set_index([thing2])
