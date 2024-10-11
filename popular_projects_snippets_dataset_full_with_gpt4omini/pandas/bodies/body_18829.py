# Extracted from ./data/repos/pandas/pandas/_testing/_warnings.py
from inspect import (
    getframeinfo,
    stack,
)

caller = getframeinfo(stack()[4][0])
msg = (
    "Warning not set with correct stacklevel. "
    f"File where warning is raised: {actual_warning.filename} != "
    f"{caller.filename}. Warning message: {actual_warning.message}"
)
assert actual_warning.filename == caller.filename, msg
