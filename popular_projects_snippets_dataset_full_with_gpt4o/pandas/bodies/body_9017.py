# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
assert case.intersect(case).equals(case)
case = case.to_block_index()
assert case.intersect(case).equals(case)
