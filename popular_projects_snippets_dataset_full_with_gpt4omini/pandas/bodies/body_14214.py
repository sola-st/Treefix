# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
df = DataFrame(np.random.random(size=(3, 3)), columns=["a", "b", "c"])

msg = (
    "Col_space length\\(\\d+\\) should match "
    "DataFrame number of columns\\(\\d+\\)"
)
with pytest.raises(ValueError, match=msg):
    df.to_html(col_space=[30, 40])

with pytest.raises(ValueError, match=msg):
    df.to_html(col_space=[30, 40, 50, 60])

msg = "unknown column"
with pytest.raises(ValueError, match=msg):
    df.to_html(col_space={"a": "foo", "b": 23, "d": 34})
