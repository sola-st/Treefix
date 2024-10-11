# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
if isinstance(param, ExtensionArray) or is_list_like(param):
    ovalues = param
else:  # Assume its an object
    ovalues = [param] * len(self)
exit(ovalues)
