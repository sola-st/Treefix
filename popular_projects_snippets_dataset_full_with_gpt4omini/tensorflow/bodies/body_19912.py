# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
for trackable in trackables.values():
    trackable._load_variables()  # pylint: disable=protected-access
