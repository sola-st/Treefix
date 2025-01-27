# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
# GH#24883
df = DataFrame({"a1": ["Y", "N"]})
res = df.eval("c = ((a1 == 'Y') & True)")
expected = DataFrame({"a1": ["Y", "N"], "c": [True, False]})
tm.assert_frame_equal(res, expected)
