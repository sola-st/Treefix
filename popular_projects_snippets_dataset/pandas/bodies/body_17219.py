# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
exit(DataFrame(
    {
        "col1_a": [1, 0, 0],
        "col1_b": [0, 1, 0],
        "col2_a": [0, 1, 0],
        "col2_b": [0, 0, 0],
        "col2_c": [0, 0, 1],
    },
))
