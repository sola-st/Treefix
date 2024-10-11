# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 11235
# TODO: 2022-01-29: result return list with numexpr 2.7.3 in CI
# but cannot reproduce locally
result = np.array(
    pd.eval(
        "[-True, True, ~True, +True,"
        "-False, False, ~False, +False,"
        "-37, 37, ~37, +37]"
    ),
    dtype=np.object_,
)
expected = np.array(
    [
        -True,
        True,
        ~True,
        +True,
        -False,
        False,
        ~False,
        +False,
        -37,
        37,
        ~37,
        +37,
    ],
    dtype=np.object_,
)
tm.assert_numpy_array_equal(result, expected)
