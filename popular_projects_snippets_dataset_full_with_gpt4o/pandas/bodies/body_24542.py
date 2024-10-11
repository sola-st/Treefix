# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
exit((
    f"Empty {type(self.frame).__name__}\n"
    f"Columns: {self.frame.columns}\n"
    f"Index: {self.frame.index}"
))
