# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# PH 24729: Unstack a df with multi level columns
df = DataFrame(
    [[0.0, 0.0], [0.0, 0.0]],
    columns=MultiIndex.from_tuples(
        [["B", "C"], ["B", "D"]], names=["c1", "c2"]
    ),
    index=MultiIndex.from_tuples(
        [[10, 20, 30], [10, 20, 40]], names=["i1", "i2", "i3"]
    ),
)
assert df.unstack(["i2", "i1"]).columns.names[-2:] == ["i2", "i1"]
