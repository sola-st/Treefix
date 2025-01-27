# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Infers steps_per_epoch needed to loop through a dataset.

  Args:
      model: Keras model instance.
      dataset: Input data of type tf.data.Dataset.
      steps: Number of steps to draw from the dataset (may be None if unknown).
      epochs: Number of times to iterate over the dataset.
      steps_name: The string name of the steps argument, either `steps`,
        `validation_steps`, or `steps_per_epoch`. Only used for error message
        formatting.

  Returns:
    Integer or `None`. Inferred number of steps to loop through the dataset.
    `None` is returned if 1) the size of the dataset is unknown and `steps` was
    not specified, or 2) this is multi-worker training and auto sharding is
    enabled.

  Raises:
    ValueError: In case of invalid argument values.
  """
assert isinstance(dataset, dataset_ops.DatasetV2)
if (model._in_multi_worker_mode() and
    (dataset.options().experimental_distribute.auto_shard_policy !=
     options_lib.AutoShardPolicy.OFF)):
    # If the dataset would be auto-sharded, we should not infer a local
    # steps_per_epoch due to the possible inbalanced sharding between workers.
    exit(None)

size = backend.get_value(cardinality.cardinality(dataset))
if size == cardinality.INFINITE and steps is None:
    raise ValueError('When passing an infinitely repeating dataset, you '
                     'must specify the `%s` argument.' % (steps_name,))
if size >= 0:
    if steps is not None and steps * epochs > size:
        if epochs > 1:
            raise ValueError('The dataset you passed contains %s batches, but you '
                             'passed `epochs=%s` and `%s=%s`, which is a total of '
                             '%s steps. We cannot draw that many steps from this '
                             'dataset. We suggest to set `%s=%s`.' %
                             (size, epochs, steps_name, steps, steps * epochs,
                              steps_name, size // epochs))
        else:
            raise ValueError('The dataset you passed contains %s batches, but you '
                             'passed `%s=%s`. We cannot draw that many steps from '
                             'this dataset. We suggest to set `%s=%s`.' %
                             (size, steps_name, steps, steps_name, size))
if steps is None:
    if size >= 0:
        exit(size)
    exit(None)
exit(steps)
