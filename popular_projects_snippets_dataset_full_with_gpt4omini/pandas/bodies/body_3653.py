# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
mapping = {"A": "a", "B": "b", "C": "c", "D": "d"}

renamed = float_frame.rename(columns=mapping)
renamed2 = float_frame.rename(columns=str.lower)

tm.assert_frame_equal(renamed, renamed2)
tm.assert_frame_equal(
    renamed2.rename(columns=str.upper), float_frame, check_names=False
)

# index
data = {"A": {"foo": 0, "bar": 1}}

# gets sorted alphabetical
df = DataFrame(data)
renamed = df.rename(index={"foo": "bar", "bar": "foo"})
tm.assert_index_equal(renamed.index, Index(["foo", "bar"]))

renamed = df.rename(index=str.upper)
tm.assert_index_equal(renamed.index, Index(["BAR", "FOO"]))

# have to pass something
with pytest.raises(TypeError, match="must pass an index to rename"):
    float_frame.rename()

# partial columns
renamed = float_frame.rename(columns={"C": "foo", "D": "bar"})
tm.assert_index_equal(renamed.columns, Index(["A", "B", "foo", "bar"]))

# other axis
renamed = float_frame.T.rename(index={"C": "foo", "D": "bar"})
tm.assert_index_equal(renamed.index, Index(["A", "B", "foo", "bar"]))

# index with name
index = Index(["foo", "bar"], name="name")
renamer = DataFrame(data, index=index)
renamed = renamer.rename(index={"foo": "bar", "bar": "foo"})
tm.assert_index_equal(renamed.index, Index(["bar", "foo"], name="name"))
assert renamed.index.name == renamer.index.name
