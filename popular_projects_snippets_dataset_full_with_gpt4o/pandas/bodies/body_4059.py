# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#16116
df = DataFrame(
    {
        "int": [1, 2, 3, 4],
        "float": [1.0, 2.0, 3.0, 4.0],
        "str": ["a", "b", "c", "d"],
    }
)
msg = "|".join(
    [
        "Could not convert",
        "could not convert",
        "can't multiply sequence by non-int",
    ]
)
with pytest.raises(TypeError, match=msg):
    getattr(df, op)()

with pd.option_context("use_bottleneck", False):
    msg = "|".join(
        [
            "Could not convert",
            "could not convert",
            "can't multiply sequence by non-int",
        ]
    )
    with pytest.raises(TypeError, match=msg):
        getattr(df, op)()
