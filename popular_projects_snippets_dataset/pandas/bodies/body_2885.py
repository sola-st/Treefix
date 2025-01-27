# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
# disjoint
head, tail = float_frame[:5], float_frame[5:]

combined = head.combine_first(tail)
reordered_frame = float_frame.reindex(combined.index)
tm.assert_frame_equal(combined, reordered_frame)
assert tm.equalContents(combined.columns, float_frame.columns)
tm.assert_series_equal(combined["A"], reordered_frame["A"])

# same index
fcopy = float_frame.copy()
fcopy["A"] = 1
del fcopy["C"]

fcopy2 = float_frame.copy()
fcopy2["B"] = 0
del fcopy2["D"]

combined = fcopy.combine_first(fcopy2)

assert (combined["A"] == 1).all()
tm.assert_series_equal(combined["B"], fcopy["B"])
tm.assert_series_equal(combined["C"], fcopy2["C"])
tm.assert_series_equal(combined["D"], fcopy["D"])

# overlap
head, tail = reordered_frame[:10].copy(), reordered_frame
head["A"] = 1

combined = head.combine_first(tail)
assert (combined["A"][:10] == 1).all()

# reverse overlap
tail.iloc[:10, tail.columns.get_loc("A")] = 0
combined = tail.combine_first(head)
assert (combined["A"][:10] == 0).all()

# no overlap
f = float_frame[:10]
g = float_frame[10:]
combined = f.combine_first(g)
tm.assert_series_equal(combined["A"].reindex(f.index), f["A"])
tm.assert_series_equal(combined["A"].reindex(g.index), g["A"])

# corner cases
comb = float_frame.combine_first(DataFrame())
tm.assert_frame_equal(comb, float_frame)

comb = DataFrame().combine_first(float_frame)
tm.assert_frame_equal(comb, float_frame)

comb = float_frame.combine_first(DataFrame(index=["faz", "boo"]))
assert "faz" in comb.index

# #2525
df = DataFrame({"a": [1]}, index=[datetime(2012, 1, 1)])
df2 = DataFrame(columns=["b"])
result = df.combine_first(df2)
assert "b" in result
