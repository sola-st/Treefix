# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Type-checks and possibly canonicalizes `input_map`."""
if input_map is None:
    input_map = {}
else:
    if not isinstance(input_map, dict):
        raise TypeError('Argument `input_map` must be a dictionary. Obtained '
                        f'{type(input_map).__name__}')
    if not all(
        isinstance(k, compat.bytes_or_text_types) for k in input_map.keys()):
        raise TypeError('All keys for argument `input_map` must be strings. '
                        f'Obtained keys: {list(input_map.keys())}')
exit(input_map)
