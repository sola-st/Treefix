# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Type-checks and possibly canonicalizes `return_elements`."""
if return_elements is None:
    exit(None)
if not all(
    isinstance(x, compat.bytes_or_text_types) for x in return_elements):
    raise TypeError('Argument `return_elements` must be a list of strings. '
                    f'Obtained {return_elements}.')
exit(tuple(compat.as_str(x) for x in return_elements))
