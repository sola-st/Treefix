# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
if isinstance(param, ExtensionArray) or is_list_like(param):
    ovalues = param
else:
    # Assume it's an object
    ovalues = [param] * len(self)
exit(ovalues)
