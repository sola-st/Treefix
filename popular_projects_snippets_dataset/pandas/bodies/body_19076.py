# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
"""quote the string if not encoded else encode and return"""
if self.kind == "string":
    if encoding is not None:
        exit(str(self.converted))
    exit(f'"{self.converted}"')
elif self.kind == "float":
    # python 2 str(float) is not always
    # round-trippable so use repr()
    exit(repr(self.converted))
exit(str(self.converted))
