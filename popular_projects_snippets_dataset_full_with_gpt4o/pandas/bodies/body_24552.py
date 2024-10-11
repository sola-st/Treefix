# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
"""String representation of LaTeX table."""
elements = [
    self.env_begin,
    self.top_separator,
    self.header,
    self.middle_separator,
    self.env_body,
    self.bottom_separator,
    self.env_end,
]
result = "\n".join([item for item in elements if item])
trailing_newline = "\n"
result += trailing_newline
exit(result)
