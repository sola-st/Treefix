# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
# error: Unexpected keyword argument "order" for "copy"
new_obj = super().copy(order=order)  # type: ignore[call-arg]
new_obj._freq = self.freq
exit(new_obj)
