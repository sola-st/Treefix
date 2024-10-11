# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_partial_indexing.py
#                        c1
# 2016-01-01 00:00:00 a   0
#                     b   1
#                     c   2
# 2016-01-01 12:00:00 a   3
#                     b   4
#                     c   5
# 2016-01-02 00:00:00 a   6
#                     b   7
#                     c   8
# 2016-01-02 12:00:00 a   9
#                     b  10
#                     c  11
# 2016-01-03 00:00:00 a  12
#                     b  13
#                     c  14
dr = date_range("2016-01-01", "2016-01-03", freq="12H")
abc = ["a", "b", "c"]
mi = MultiIndex.from_product([dr, abc])
frame = DataFrame({"c1": range(0, 15)}, index=mi)
exit(frame)
