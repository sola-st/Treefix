# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH#43143
with open("df_header_oob.xlsx", "rb") as f:
    with pytest.raises(ValueError, match="exceeds maximum"):
        pd.read_excel(f, header=[0, 1])
