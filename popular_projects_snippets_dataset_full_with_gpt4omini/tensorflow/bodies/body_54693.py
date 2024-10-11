# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/random_seed.py
"""Returns the local seeds an operation should use given an op-specific seed.

  Given operation-specific seed, `op_seed`, this helper function returns two
  seeds derived from graph-level and op-level seeds. Many random operations
  internally use the two seeds to allow user to change the seed globally for a
  graph, or for only specific operations.

  For details on how the graph-level seed interacts with op seeds, see
  `tf.compat.v1.random.set_random_seed`.

  Args:
    op_seed: integer.

  Returns:
    A tuple of two integers that should be used for the local seed of this
    operation.
  """
eager = context.executing_eagerly()

if eager:
    global_seed = context.global_seed()
else:
    global_seed = ops.get_default_graph().seed

if global_seed is not None:
    if op_seed is None:
        # pylint: disable=protected-access
        if hasattr(ops.get_default_graph(), '_seed_used'):
            ops.get_default_graph()._seed_used = True
        if eager:
            op_seed = context.internal_operation_seed()
        else:
            op_seed = _graph_to_seed_dict.setdefault(ops.get_default_graph(), 0)
            _graph_to_seed_dict[ops.get_default_graph()] += 1

    seeds = _truncate_seed(global_seed), _truncate_seed(op_seed)
else:
    if op_seed is not None:
        seeds = DEFAULT_GRAPH_SEED, _truncate_seed(op_seed)
    else:
        seeds = None, None

if seeds == (None, None) and config.is_op_determinism_enabled():
    raise RuntimeError(  # pylint: disable=g-doc-exception
        'Random ops require a seed to be set when determinism is enabled. '
        'Please set a seed before running the op, e.g. by calling '
        'tf.random.set_seed(1).')

# Avoid (0, 0) as the C++ ops interpret it as nondeterminism, which would
# be unexpected since Python docs say nondeterminism is (None, None).
if seeds == (0, 0):
    exit((0, _MAXINT32))
exit(seeds)
