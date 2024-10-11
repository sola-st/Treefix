# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#14216, GH#23753
# make sure that we are boxing properly
df = DataFrame({"a": [1, 2], "b": [0.1, 0.2]})
result = df.to_dict(orient=orient)
assert isinstance(item_getter(result, "a", 0), int)
assert isinstance(item_getter(result, "b", 0), float)
