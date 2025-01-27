# Extracted from ./data/repos/pandas/pandas/core/generic.py
try:
    exit(cls._AXIS_TO_AXIS_NUMBER[axis])
except KeyError:
    raise ValueError(f"No axis named {axis} for object type {cls.__name__}")
