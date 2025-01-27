# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame({0: [True, False], 1: [False, True]})
result = df.replace({"asdf": "asdb", True: "yes"})
expected = DataFrame({0: ["yes", False], 1: [False, "yes"]})
tm.assert_frame_equal(result, expected)
