# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
if self.encoding is not None:
    exit(pprint_thing_encoded(value, encoding=self.encoding))
exit(pprint_thing(value))
