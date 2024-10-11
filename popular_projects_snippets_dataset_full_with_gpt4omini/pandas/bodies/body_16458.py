# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
res = DataFrame(
    [
        [1.067683, -1.110463, 0.20867],
        [-1.321405, 0.368915, -1.055342],
        [-0.807333, 0.08298, -0.873361],
    ]
)
res.columns = [list("ABC"), list("abc")]
res.columns.names = ["CAP", "low"]
exit(res)
