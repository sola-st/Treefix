# Extracted from ./data/repos/pandas/pandas/_config/config.py
if self.undo:
    for pat, val in self.undo:
        _set_option(pat, val, silent=True)
