# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
# Validate configurations.
if isinstance(curve, metrics_utils.AUCCurve) and curve not in list(
    metrics_utils.AUCCurve):
    raise ValueError('Invalid curve: "{}". Valid options are: "{}"'.format(
        curve, list(metrics_utils.AUCCurve)))
if isinstance(
    summation_method,
    metrics_utils.AUCSummationMethod) and summation_method not in list(
        metrics_utils.AUCSummationMethod):
    raise ValueError(
        'Invalid summation method: "{}". Valid options are: "{}"'.format(
            summation_method, list(metrics_utils.AUCSummationMethod)))

# Update properties.
if thresholds is not None:
    # If specified, use the supplied thresholds.
    self.num_thresholds = len(thresholds) + 2
    thresholds = sorted(thresholds)
    self._thresholds_distributed_evenly = (
        metrics_utils.is_evenly_distributed_thresholds(
            np.array([0.0] + thresholds + [1.0])))
else:
    if num_thresholds <= 1:
        raise ValueError('`num_thresholds` must be > 1.')

    # Otherwise, linearly interpolate (num_thresholds - 2) thresholds in
    # (0, 1).
    self.num_thresholds = num_thresholds
    thresholds = [(i + 1) * 1.0 / (num_thresholds - 1)
                  for i in range(num_thresholds - 2)]
    self._thresholds_distributed_evenly = True

# Add an endpoint "threshold" below zero and above one for either
# threshold method to account for floating point imprecisions.
self._thresholds = np.array([0.0 - backend.epsilon()] + thresholds +
                            [1.0 + backend.epsilon()])

if isinstance(curve, metrics_utils.AUCCurve):
    self.curve = curve
else:
    self.curve = metrics_utils.AUCCurve.from_str(curve)
if isinstance(summation_method, metrics_utils.AUCSummationMethod):
    self.summation_method = summation_method
else:
    self.summation_method = metrics_utils.AUCSummationMethod.from_str(
        summation_method)
super(AUC, self).__init__(name=name, dtype=dtype)

# Handle multilabel arguments.
self.multi_label = multi_label
if label_weights is not None:
    label_weights = constant_op.constant(label_weights, dtype=self.dtype)
    checks = [
        check_ops.assert_non_negative(
            label_weights,
            message='All values of `label_weights` must be non-negative.')
    ]
    with ops.control_dependencies(checks):
        self.label_weights = label_weights

else:
    self.label_weights = None

self._from_logits = from_logits

self._built = False
if self.multi_label:
    if num_labels:
        shape = tensor_shape.TensorShape([None, num_labels])
        self._build(shape)
else:
    if num_labels:
        raise ValueError(
            '`num_labels` is needed only when `multi_label` is True.')
    self._build(None)
