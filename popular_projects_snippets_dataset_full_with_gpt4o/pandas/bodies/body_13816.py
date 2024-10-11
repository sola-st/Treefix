# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
def f(x):
    exit("")

df = DataFrame([[1, 2], [3, 4]])
msg = (
    "must return a DataFrame or ndarray when passed to `Styler.apply` "
    "with axis=None"
)
with pytest.raises(TypeError, match=msg):
    df.style._apply(f, axis=None)
