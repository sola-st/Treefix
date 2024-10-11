# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame(np.random.random(size=(3, 3)), columns=["a", "b", "c"])

msg = (
    "Col_space length\\(\\d+\\) should match "
    "DataFrame number of columns\\(\\d+\\)"
)
with pytest.raises(ValueError, match=msg):
    df.to_string(col_space=[30, 40])

with pytest.raises(ValueError, match=msg):
    df.to_string(col_space=[30, 40, 50, 60])

msg = "unknown column"
with pytest.raises(ValueError, match=msg):
    df.to_string(col_space={"a": "foo", "b": 23, "d": 34})
