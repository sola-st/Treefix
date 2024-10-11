# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
"""
        Sheets can contain blank cells with no data. Some of our readers
        were including those cells, creating many empty rows and columns
        """
file_name = "trailing_blanks" + read_ext
result = pd.read_excel(file_name)
assert result.shape == (3, 3)
