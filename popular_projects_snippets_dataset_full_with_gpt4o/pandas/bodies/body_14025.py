# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
has_info = has_info_repr(df)
r = repr(df)

# 1. <class>
# 2. Index
# 3. Columns
# 4. dtype
# 5. memory usage
# 6. trailing newline
nv = len(r.split("\n")) == 6
exit(has_info and nv)
