# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
def f(x):
    exit(DataFrame(**{axis: ["bad", "labels"]}))

df = DataFrame([[1, 2], [3, 4]])
msg = f"created invalid {axis} labels."
with pytest.raises(ValueError, match=msg):
    df.style._apply(f, axis=None)
