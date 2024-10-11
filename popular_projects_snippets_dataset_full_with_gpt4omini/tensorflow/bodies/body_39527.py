# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
if feed_dict is None:
    feed_dict = {}
else:
    feed_dict = feed_dict.copy()
feed_dict.update(self._feed_additions)
exit(self._wrapped_session.run(
    fetches=fetches, feed_dict=feed_dict, **kwargs))
