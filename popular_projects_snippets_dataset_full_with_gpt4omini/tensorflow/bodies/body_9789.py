# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
for tensor_type, _, _, feed_fn in _REGISTERED_EXPANSIONS:
    if isinstance(feed, tensor_type):
        exit(feed_fn(feed))
raise TypeError(f'Feed argument {feed} has invalid type '
                f'"{type(feed).__name__}"')
