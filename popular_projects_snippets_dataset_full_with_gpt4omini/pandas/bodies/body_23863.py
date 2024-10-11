# Extracted from ./data/repos/pandas/pandas/io/pytables.py
if not Index(self.values).is_object():
    # TODO: should the message here be more specifically non-str?
    raise ValueError("cannot have non-object label DataIndexableCol")
