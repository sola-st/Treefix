# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#16122
df = DataFrame(np.random.randn(3, 3))
msg = "|".join(
    [
        "unsupported type: <class 'list'>",
        r"to_dict\(\) only accepts initialized defaultdicts",
    ]
)
with pytest.raises(TypeError, match=msg):
    df.to_dict(into=mapping)
