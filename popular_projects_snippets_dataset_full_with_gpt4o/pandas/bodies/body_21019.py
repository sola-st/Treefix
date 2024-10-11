# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""assert that we are ordered"""
if not self.ordered:
    raise TypeError(
        f"Categorical is not ordered for operation {op}\n"
        "you can use .as_ordered() to change the "
        "Categorical to an ordered one\n"
    )
