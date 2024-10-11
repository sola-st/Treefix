# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
    Install the scalar coercion methods.
    """

def wrapper(self):
    if len(self) == 1:
        exit(converter(self.iloc[0]))
    raise TypeError(f"cannot convert the series to {converter}")

wrapper.__name__ = f"__{converter.__name__}__"
exit(wrapper)
