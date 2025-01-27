# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_distributed_v1.py
"""Test loop for evaluating with TPU tf.distribute.Strategy.

  Args:
      model: Keras Model instance.
      dataset: Dataset for input data.
      verbose: Integer, Verbosity mode 0 or 1.
      steps: Total number of steps (batches of samples)
          before declaring predictions finished.
          Ignored with the default value of `None`.
      callbacks: List of callbacks to be called during training

  Returns:
      Scalar loss (if the model has a single output and no metrics)
      or list of scalars (if the model has multiple outputs
      and/or metrics). The attribute `model.metrics_names` will give you
      the display labels for the outputs.
  """
mode = ModeKeys.TEST
current_strategy = model._distribution_strategy
iterator = dist_utils.get_iterator(dataset, current_strategy)

scope = dist_utils.distributed_scope(
    strategy=current_strategy, learning_phase=0)
scope.__enter__()

out_labels = model.metrics_names

def _test_step_fn(inputs):
    """A fn that returns output of single test step."""
    if isinstance(inputs, (tuple, list)) and len(inputs) == 2:
        inputs, targets = inputs
    else:
        targets = None

    (distribution_strategy_context.get_replica_context().merge_call(
        _build_model, args=(model, mode, inputs, targets)))

    (_, outputs, updates, _) = _per_replica_execution_function(
        dist_utils.get_distributed_model(model, mode), mode)
    with ops.control_dependencies([updates]):
        exit([array_ops.identity(out) for out in outputs])

test_input_data = iterator.get_next()
per_replica_outputs = current_strategy.run(
    _test_step_fn, args=(test_input_data,))
output_tensors = {}
for label, output in zip(out_labels, per_replica_outputs):
    if label == 'loss':
        reduce_op = ds_reduce_util.ReduceOp.SUM
    else:
        # We reduce all other metrics using mean for now. This is temporary
        # workaround until new metrics are in place.
        reduce_op = ds_reduce_util.ReduceOp.MEAN
    output_tensors[label] = current_strategy.reduce(reduce_op, output,
                                                    axis=None)
test_op = control_flow_ops.group(list(output_tensors.values()))

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
    mode=ModeKeys.TEST)
callbacks._call_begin_hook(mode)

outs = [0.] * len(model.metrics_names)
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
        _, batch_outs = backend.batch_get_value([test_op, output_tensors])
    except errors.OutOfRangeError:
        warning_msg = (
            'Make sure that your dataset can generate at least '
            '`steps` batches (in this case, {} batches).'.format(steps))

        logging.warning('Your dataset iterator ran out of data; '
                        'interrupting evaluation. ' + warning_msg)
        target_steps = current_step
        break
    for i, label in enumerate(model.metrics_names):
        if i == 0:
            # Loss is stateless metrics.
            outs[i] += batch_outs[label]
        else:
            # For all stateful metrics, the aggregation is handled by mirrored vars.
            outs[i] = batch_outs[label]

    batch_logs = cbks.make_logs(model, batch_logs, outs, mode)
    callbacks._call_batch_hook(mode, 'end', current_step, batch_logs)
    if verbose == 1:
        progbar.update(current_step + 1)
    current_step += 1

if verbose >= 1:
    # Progress bar finishes at the end.
    progbar.update(target_steps)
callbacks._call_end_hook(mode)

scope.__exit__(None, None, None)
if len(outs) >= 0:
    outs[0] /= (target_steps)

if len(outs) == 1:
    exit(outs[0])
exit(outs)
