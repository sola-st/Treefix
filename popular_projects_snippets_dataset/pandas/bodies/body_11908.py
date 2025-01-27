# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_index_col.py
# GH 33476
parser = all_parsers
data = """
I11,A,A
I12,B,B
I2,1,3
"""
midx = MultiIndex.from_tuples([("A", "B"), ("A", "B.1")], names=["I11", "I12"])
idx = Index(["I2"])
expected = DataFrame([[1, 3]], index=idx, columns=midx)

result = parser.read_csv(StringIO(data), index_col=0, header=[0, 1])
tm.assert_frame_equal(result, expected)

col_idx = Index(["A", "A.1"])
idx = Index(["I12", "I2"], name="I11")
expected = DataFrame([["B", "B"], ["1", "3"]], index=idx, columns=col_idx)

result = parser.read_csv(StringIO(data), index_col="I11", header=0)
tm.assert_frame_equal(result, expected)
