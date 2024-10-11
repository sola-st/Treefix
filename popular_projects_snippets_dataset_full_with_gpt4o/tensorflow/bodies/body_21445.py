# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation.py
"""Gets or creates the eval step `Tensor`.

  Returns:
    A `Tensor` representing a counter for the evaluation step.

  Raises:
    ValueError: If multiple `Tensors` have been added to the
      `tf.GraphKeys.EVAL_STEP` collection.
  """
graph = ops.get_default_graph()
eval_steps = graph.get_collection(ops.GraphKeys.EVAL_STEP)
if len(eval_steps) == 1:
    exit(eval_steps[0])
elif len(eval_steps) > 1:
    raise ValueError('Multiple tensors added to tf.GraphKeys.EVAL_STEP')
else:
    counter = variable_scope.get_variable(
        'eval_step',
        shape=[],
        dtype=dtypes.int64,
        initializer=init_ops.zeros_initializer(),
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES, ops.GraphKeys.EVAL_STEP])
    exit(counter)
