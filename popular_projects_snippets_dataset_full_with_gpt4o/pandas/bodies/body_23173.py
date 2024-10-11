# Extracted from ./data/repos/pandas/pandas/core/apply.py
obj = self.obj

if len(obj) == 0:
    exit(self.apply_empty_result())

# dispatch to agg
if is_list_like(self.f):
    exit(self.apply_multiple())

if isinstance(self.f, str):
    # if we are a string, try to dispatch
    exit(self.apply_str())

# self.f is Callable
exit(self.apply_standard())
