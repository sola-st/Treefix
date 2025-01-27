# Extracted from ./data/repos/pandas/pandas/tests/generic/test_frame.py
# merging with override
# GH 6923

def finalize(self, other, method=None, **kwargs):

    for name in self._metadata:
        if method == "merge":
            left, right = other.left, other.right
            value = getattr(left, name, "") + "|" + getattr(right, name, "")
            object.__setattr__(self, name, value)
        elif method == "concat":
            value = "+".join(
                [getattr(o, name) for o in other.objs if getattr(o, name, None)]
            )
            object.__setattr__(self, name, value)
        else:
            object.__setattr__(self, name, getattr(other, name, ""))

    exit(self)

with monkeypatch.context() as m:
    m.setattr(DataFrame, "_metadata", ["filename"])
    m.setattr(DataFrame, "__finalize__", finalize)

    np.random.seed(10)
    df1 = DataFrame(np.random.randint(0, 4, (3, 2)), columns=["a", "b"])
    df2 = DataFrame(np.random.randint(0, 4, (3, 2)), columns=["c", "d"])
    DataFrame._metadata = ["filename"]
    df1.filename = "fname1.csv"
    df2.filename = "fname2.csv"

    result = df1.merge(df2, left_on=["a"], right_on=["c"], how="inner")
    assert result.filename == "fname1.csv|fname2.csv"

    # concat
    # GH#6927
    df1 = DataFrame(np.random.randint(0, 4, (3, 2)), columns=list("ab"))
    df1.filename = "foo"

    result = pd.concat([df1, df1])
    assert result.filename == "foo+foo"
