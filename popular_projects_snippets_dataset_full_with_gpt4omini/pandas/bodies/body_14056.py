# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame(np.random.random(size=(1, 3)))
c10 = len(df.to_string(col_space=10).split("\n")[1])
c20 = len(df.to_string(col_space=20).split("\n")[1])
c30 = len(df.to_string(col_space=30).split("\n")[1])
assert c10 < c20 < c30

# GH 8230
# col_space wasn't being applied with header=False
with_header = df.to_string(col_space=20)
with_header_row1 = with_header.splitlines()[1]
no_header = df.to_string(col_space=20, header=False)
assert len(with_header_row1) == len(no_header)
