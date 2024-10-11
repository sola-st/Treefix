# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 21696
df = DataFrame({"a": ["x", "y", "z"]})
expected = """\
manual header
x
y
z
"""
with tm.ensure_clean("test.txt") as path:
    with open(path, "w") as f:
        f.write("manual header\n")
        df.to_csv(f, header=None, index=None)
    with open(path) as f:
        assert f.read() == expected
