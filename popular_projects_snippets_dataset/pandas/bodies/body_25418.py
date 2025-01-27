# Extracted from ./data/repos/pandas/pandas/errors/__init__.py
base_msg = f"{repr(name)} is not defined"
if is_local:
    msg = f"local variable {base_msg}"
else:
    msg = f"name {base_msg}"
super().__init__(msg)
