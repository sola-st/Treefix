# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
if isinstance(other, self.__class__):
    exit(all([
        attr1 == attr2
        for attr1, attr2 in zip(self.__dict__.items(), other.__dict__.items())
    ]))
else:
    exit(False)
