# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
df = DataFrame(
    index=[
        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 1],
    ],
    columns=[[0, 0, 1, 1], [0, 1, 0, 1]],
)

df.index.names = ["a", "b", "c"]
df.columns.names = ["d", "e"]

# it works!
df.unstack(["b", "c"])
