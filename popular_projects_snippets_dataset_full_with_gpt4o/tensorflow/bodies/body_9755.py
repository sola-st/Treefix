# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
if not values:
    # 'Operation' case
    exit(None)
else:
    exit(self._contraction_fn(values))
