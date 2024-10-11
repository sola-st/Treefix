# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Create an OrderedDict from Dict."""
exit(collections.OrderedDict((k, d[k]) for k in sorted(d)))
