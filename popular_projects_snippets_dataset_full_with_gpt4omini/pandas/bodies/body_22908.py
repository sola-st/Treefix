# Extracted from ./data/repos/pandas/pandas/core/generic.py
raise ValueError(
    f"The truth value of a {type(self).__name__} is ambiguous. "
    "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
)
