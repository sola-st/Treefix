# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH: 26861
data = [Period("2003-12", "D")]
result = DataFrame([])
result["a"] = data

expected = DataFrame({"a": data})

tm.assert_frame_equal(result, expected)
