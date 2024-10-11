# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
df = DataFrame(
    {
        "int": [1, 2, 3],
        "float": [1.0, 2.0, 3.0],
        "object": [(1, 2), True, False],
    },
    columns=["int", "float", "object"],
)

formatters = [
    ("int", lambda x: f"0x{x:x}"),
    ("float", lambda x: f"[{x: 4.1f}]"),
    ("object", lambda x: f"-{x!s}-"),
]
result = df.to_string(formatters=dict(formatters))
result2 = df.to_string(formatters=list(zip(*formatters))[1])
assert result == (
    "  int  float    object\n"
    "0 0x1 [ 1.0]  -(1, 2)-\n"
    "1 0x2 [ 2.0]    -True-\n"
    "2 0x3 [ 3.0]   -False-"
)
assert result == result2
