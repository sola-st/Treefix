# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(CategoricalCrossentropy, self).__init__(
    categorical_crossentropy,
    name,
    dtype=dtype,
    from_logits=from_logits,
    label_smoothing=label_smoothing)
