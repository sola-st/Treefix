# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
encoder: Callable
if self.encoding is not None:
    encoder = partial(pprint_thing_encoded, encoding=self.encoding)
else:
    encoder = pprint_thing
exit(encoder(value))
