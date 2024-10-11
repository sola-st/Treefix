# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_explode.py
# GH 28005
df = pd.DataFrame(input_dict, index=input_index)
result = df.explode("col1")
expected = pd.DataFrame(expected_dict, index=expected_index, dtype=object)
tm.assert_frame_equal(result, expected)
