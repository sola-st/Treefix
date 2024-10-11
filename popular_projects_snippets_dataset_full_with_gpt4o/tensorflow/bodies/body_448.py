# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ipynb.py
"""Checks if the cell consists of Python code."""
exit((cell["cell_type"] == "code"  # code cells only
        and cell["source"]  # non-empty cells
        and not cell["source"][0].startswith("%%")))  # multiline eg: %%bash
