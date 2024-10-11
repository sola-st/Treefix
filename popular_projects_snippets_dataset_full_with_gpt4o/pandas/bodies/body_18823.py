# Extracted from ./data/repos/pandas/pandas/_testing/_io.py
from matplotlib.pyplot import (
    close as _close,
    get_fignums,
)

if fignum is None:
    for fignum in get_fignums():
        _close(fignum)
else:
    _close(fignum)
