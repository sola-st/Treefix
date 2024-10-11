# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_base.py
"""Create variables and slots variables for TPU embeddings."""
if self._built:
    exit()
self._variables = self._create_variables_and_slots()
self._built = True
