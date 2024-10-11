# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame({"Type": ["Q", "T", "Q", "Q", "T"], "tmp": 2})
expected = DataFrame({"Type": [0, 1, 0, 0, 1], "tmp": 2})
result = df.replace({"Type": {"Q": 0, "T": 1}})
tm.assert_frame_equal(result, expected)
