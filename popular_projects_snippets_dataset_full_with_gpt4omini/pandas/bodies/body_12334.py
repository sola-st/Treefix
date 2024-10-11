# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 13923, 25772
msg = """
Value labels for column ethnicsn are not unique. These cannot be converted to
pandas categoricals.

Either read the file with `convert_categoricals` set to False or use the
low level interface in `StataReader` to separately read the values and the
value_labels.

The repeated labels are:\n-+\nwolof
"""
with pytest.raises(ValueError, match=msg):
    read_stata(
        datapath("io", "data", "stata", "stata15.dta"),
        convert_categoricals=True,
    )
