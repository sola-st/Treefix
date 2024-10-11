# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_distributed_v1.py
"""Predict loop for predicting with TPU tf.distribute.Strategy.

  Args:
      model: Keras Model instance.
      dataset: Dataset for input data.
      verbose: Integer, Verbosity mode 0 or 1.
      steps: Total number of steps (batches of samples)
          before declaring `_predict_loop` finished.
          Ignored with the default value of `None`.
      callbacks: List of callbacks to be called during training

  Returns:
      Array of predictions (if the model has a single output)
      or list of arrays of predictions
      (if the model has multiple outputs).
  """
mode = ModeKeys.PREDICT
dataset_fully_shaped = dist_utils.is_dataset_shape_fully_defined(dataset)
padding_handler = None
if not dataset_fully_shaped:
    # TODO(hongjunchoi): Investigate whether operations from
    # PartialBatchPaddingHandler are unnecessarily pruned out
    # during graph optimization.
    padding_handler = padding_util.PartialBatchPaddingHandler(
        model._feed_output_shapes)
    batch_size, _, prefetch_buffer = input_lib._get_dataset_attributes(dataset)
    padding_handler.padded_batch_size = batch_size
    padding_handler.padding_mask = dataset.reduce(padding_handler.padding_mask,
                                                  padding_handler.update_mask)

    dataset = dataset.map(padding_handler.pad_batch)
    dataset = dataset.unbatch()
    # Upon this point, it is guaranteed that the dataset does not
    # have partial batches. Thus, we set `drop_remainder=True` to
    # get static shape information about the elements in the dataset.
    dataset = dataset.batch(batch_size, drop_remainder=True)

    if prefetch_buffer is not None:
        dataset = dataset.prefetch(prefetch_buffer)

current_strategy = model._distribution_strategy
iterator = dist_utils.get_iterator(dataset, current_strategy)

scope = dist_utils.distributed_scope(
    strategy=current_strategy, learning_phase=0)
scope.__enter__()

def _predict_step_fn(inputs):
    """A fn that returns output of single prediction step."""

    (distribution_strategy_context.get_replica_context().merge_call(
        _build_model, args=(model, mode, inputs)))

    (_, outputs, updates, _) = _per_replica_execution_function(
        dist_utils.get_distributed_model(model, mode), mode)

    with ops.control_dependencies([updates]):
        exit([array_ops.identity(out) for out in outputs])

  # TODO(hongjunchoi): When numpy array is passed as an input to `predict()`
  # use numpy arrays directly to avoid cumulating unnecessary input pipeline
  # ops.
predict_input_data = iterator.get_next()
per_replica_outputs = current_strategy.run(
    _predict_step_fn, args=(predict_input_data,))
output_tensors = dist_utils.flatten_per_replica_values(
    current_strategy, per_replica_outputs)

if verbose >= 1:
    progbar = Progbar(target=steps)

if model._compile_distribution:
    dist_utils._copy_weights_to_distributed_model(model, mode)

dist_utils._reset_metrics(model)

callbacks = cbks.configure_callbacks(
    callbacks,
    model,
    do_validation=False,
    epochs=1,
    steps_per_epoch=steps,
    verbose=verbose,
    count_mode='steps',
    mode=mode)
callbacks._call_begin_hook(mode)

# Since we do not know how many samples we will see, we cannot pre-allocate
# the returned Numpy arrays. Instead, we store one array per batch seen
# and concatenate them upon returning.
num_model_outputs = len(model.output_names)
unconcatenated_outs = [[] for _ in range(num_model_outputs)]
if steps is not None:
    target_steps = steps
else:
    raise ValueError('Number of steps could not be inferred from the data, '
                     'please pass the steps argument.')

current_step = 0
while current_step < target_steps:
    batch_logs = {'batch': current_step, 'size': 1}
    callbacks._call_batch_hook(mode, 'begin', current_step, batch_logs)
    try:
        predict_ops = control_flow_ops.group(output_tensors)
        _, batch_outs = backend.batch_get_value([predict_ops, output_tensors])

    except errors.OutOfRangeError:
        warning_msg = (
            'Make sure that your dataset can generate at least '
            '`steps` batches (in this case, {} batches).'.format(steps))

        logging.warning('Your dataset iterator ran out of data; '
                        'interrupting evaluation. ' + warning_msg)
        break

    # TODO(priyag): maybe need to unwrap the outputs first for MirroredStrategy.
    for i in range(num_model_outputs):
        output_start_index = i * current_strategy.num_replicas_in_sync
        output_end_index = (
            output_start_index + current_strategy.num_replicas_in_sync)
        single_model_output = batch_outs[output_start_index:output_end_index]
        unconcatenated_outs[i].extend(single_model_output)

    batch_logs = cbks.make_logs(model, batch_logs, batch_outs, mode)
    callbacks._call_batch_hook(mode, 'end', current_step, batch_logs)
    if verbose == 1:
        progbar.update(current_step + 1)
    current_step += 1

if verbose >= 1:
    # Progress bar finishes at the end.
    progbar.update(current_step)

callbacks._call_end_hook(mode)

scope.__exit__(None, None, None)

if len(unconcatenated_outs) == 1:
    prediction_result = np.concatenate(unconcatenated_outs[0], axis=0)
else:
    prediction_result = [
        np.concatenate(out, axis=0) for out in unconcatenated_outs
    ]

if padding_handler:
    prediction_result = padding_handler.apply_mask(prediction_result)

exit(prediction_result)
