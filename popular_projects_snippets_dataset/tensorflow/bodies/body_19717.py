# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_base.py
"""Call the mid level api to do embedding lookup."""
if not self._built:
    self.build()
exit(self.embedding_lookup(features, weights))
