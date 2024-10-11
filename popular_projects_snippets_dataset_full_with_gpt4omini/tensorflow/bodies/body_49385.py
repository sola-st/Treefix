# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(MeanTensor, self).__init__(name=name, dtype=dtype)
self._shape = None
self._total = None
self._count = None
self._built = False
if shape is not None:
    self._build(shape)
