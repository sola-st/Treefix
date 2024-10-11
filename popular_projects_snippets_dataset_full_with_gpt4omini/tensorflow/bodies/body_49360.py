# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Initialize TP, FP, TN, and FN tensors, given the shape of the data."""
if self.multi_label:
    if shape.ndims != 2:
        raise ValueError('`y_true` must have rank=2 when `multi_label` is '
                         'True. Found rank %s.' % shape.ndims)
    self._num_labels = shape[1]
    variable_shape = tensor_shape.TensorShape(
        [tensor_shape.Dimension(self.num_thresholds), self._num_labels])

else:
    variable_shape = tensor_shape.TensorShape(
        [tensor_shape.Dimension(self.num_thresholds)])
self._build_input_shape = shape
# Create metric variables
self.true_positives = self.add_weight(
    'true_positives',
    shape=variable_shape,
    initializer=init_ops.zeros_initializer)
self.true_negatives = self.add_weight(
    'true_negatives',
    shape=variable_shape,
    initializer=init_ops.zeros_initializer)
self.false_positives = self.add_weight(
    'false_positives',
    shape=variable_shape,
    initializer=init_ops.zeros_initializer)
self.false_negatives = self.add_weight(
    'false_negatives',
    shape=variable_shape,
    initializer=init_ops.zeros_initializer)

if self.multi_label:
    with ops.init_scope():
        # This should only be necessary for handling v1 behavior. In v2, AUC
        # should be initialized outside of any tf.functions, and therefore in
        # eager mode.
        if not context.executing_eagerly():
            backend._initialize_variables(backend._get_session())  # pylint: disable=protected-access

self._built = True
