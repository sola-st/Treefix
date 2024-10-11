# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
"""
        Test to ensure category dtypes are maintained
        after replace with dict values
        """
# GH#35268, GH#44940

# create input dataframe
input_dict = {"col1": ["a"], "col2": ["obj1"], "col3": ["cat1"]}
# explicitly cast columns as category
input_df = DataFrame(data=input_dict).astype(
    {"col1": "category", "col2": "category", "col3": "category"}
)

# create expected dataframe
expected_dict = {"col1": ["z"], "col2": ["obj9"], "col3": ["catX"]}
# explicitly cast columns as category
expected = DataFrame(data=expected_dict).astype(
    {"col1": "category", "col2": "category", "col3": "category"}
)

# replace values in input dataframe using a dict
result = input_df.replace({"a": "z", "obj1": "obj9", "cat1": "catX"})

tm.assert_frame_equal(result, expected)
