# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
if target is not None:
    # We need to use `y` to set the model targets.
    if training_utils_v1.has_tensors(target):
        target = training_utils_v1.cast_if_floating_dtype_and_mismatch(
            target, self.outputs)
    training_utils_v1.validate_input_types(
        target, orig_target, allow_dict=False, field_name='target')
    if isinstance(target, (list, tuple)):
        all_inputs += list(target)
    else:
        all_inputs.append(target)
    # Type check that all inputs are *either* value *or* symbolic.
    # TODO(fchollet): this check could be removed in Eager mode?
if any(tensor_util.is_tf_type(v) for v in all_inputs):
    if not all(tensor_util.is_tf_type(v) for v in all_inputs):
        raise ValueError('Do not pass inputs that mix Numpy arrays and '
                         'TensorFlow tensors. '
                         'You passed: x=' + str(orig_inputs) +
                         '; y=' + str(orig_target))
is_dataset = isinstance(orig_inputs, (dataset_ops.DatasetV1,
                                      dataset_ops.DatasetV2,
                                      iterator_ops.Iterator))
if is_dataset or context.executing_eagerly():
    target_tensors = None
else:
    # Handle target tensors if any passed.
    if target is not None:
        if not isinstance(target, (list, tuple)):
            target = [target]
        target_tensors = [v for v in target if _is_symbolic_tensor(v)]
    else:
        target_tensors = None

self.compile(
    optimizer=self.optimizer,
    loss=self.loss,
    metrics=self._compile_metrics,
    weighted_metrics=self._compile_weighted_metrics,
    loss_weights=self.loss_weights,
    target_tensors=target_tensors,
    sample_weight_mode=self.sample_weight_mode,
    run_eagerly=self.run_eagerly,
    experimental_run_tf_function=self._experimental_run_tf_function)
