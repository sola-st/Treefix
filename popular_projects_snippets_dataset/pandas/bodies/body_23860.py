# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""validate that we have the same order as the existing & same dtype"""
if append:
    existing_fields = getattr(self.attrs, self.kind_attr, None)
    if existing_fields is not None and existing_fields != list(self.values):
        raise ValueError("appended items do not match existing items in table!")

    existing_dtype = getattr(self.attrs, self.dtype_attr, None)
    if existing_dtype is not None and existing_dtype != self.dtype:
        raise ValueError(
            "appended items dtype do not match existing items dtype in table!"
        )
