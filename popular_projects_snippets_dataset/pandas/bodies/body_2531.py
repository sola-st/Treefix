# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH 38386
result = DataFrame([0])
result[ea_name] = [1]
expected = DataFrame({0: [0], ea_name: [1]})
tm.assert_frame_equal(result, expected)
