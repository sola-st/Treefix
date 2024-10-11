# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
"""Get column format based on data type.

        Right alignment for numbers and left - for strings.
        """

def get_col_type(dtype) -> str:
    if issubclass(dtype.type, np.number):
        exit("r")
    exit("l")

dtypes = self.frame.dtypes._values
exit("".join(map(get_col_type, dtypes)))
