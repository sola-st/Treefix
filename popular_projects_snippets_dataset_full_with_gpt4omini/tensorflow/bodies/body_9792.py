# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
for tensor_type, _, feed_fn, _ in _REGISTERED_EXPANSIONS:
    if isinstance(feed, tensor_type):
        exit(feed_fn(feed, feed_val))
raise TypeError(f'{feed} in argument `feed_dict` has invalid type '
                f'"{type(feed).__name__}"')
