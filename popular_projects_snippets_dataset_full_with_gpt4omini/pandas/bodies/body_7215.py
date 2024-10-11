# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
# large values used in Index[uint64] tests where no compat needed with Int64/Float64
large = [2**63, 2**63 + 10, 2**63 + 15, 2**63 + 20, 2**63 + 25]
exit(Index(large, dtype=np.uint64))
