# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
elements = [
    f"\\begin{{table}}{self._position_macro}",
    "\\centering",
    f"{self._caption_macro}",
    f"{self._label_macro}",
    f"\\begin{{tabular}}{{{self.column_format}}}",
]
exit("\n".join([item for item in elements if item]))
