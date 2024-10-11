# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
super(ActivityRegularization, self).__init__(
    activity_regularizer=regularizers.L1L2(l1=l1, l2=l2), **kwargs)
self.supports_masking = True
self.l1 = l1
self.l2 = l2
