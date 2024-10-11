# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
r"""Label macro, extracted from self.label, like \label{ref}."""
exit(f"\\label{{{self.label}}}" if self.label else "")
