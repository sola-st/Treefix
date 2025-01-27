# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Functional form of a while statement.

  The loop operates on a so-called state, which includes all symbols that are
  variant across loop iterations. In what follows we refer to state as either
  a tuple of entities that represent an actual state, or a list of arguments
  of the corresponding types.

  The inputs and outputs of the callables representing the loop blocks are not
  explicit - instead, these functions must use nonlocal/global for side effects.
  The inputs and outputs are instead controlled by the set_state/get_state
  functions.

  Args:
    test: Callable with boolean return type. The loop condition.
    body: Callable representing the actual loop body.
    get_state: Additional callable which can capture additional state (such as
      the values of composite symbols). This is only useful when staging the
      loop.
    set_state: Additional callable which save values captured by get_state back
      into the Python environment. This is only useful when staging the loop.
    symbol_names: Tuple containing the names of all loop variables.
    opts: Optional dict of extra loop parameters.

  Returns:
    Tuple containing the final state.
  """

# Evaluate the initial test once in order to do the dispatch. The evaluation
# is isolated to minimize unwanted side effects.
# TODO(mdan): Do a full iteration - some state types might lower to Tensor.
with func_graph.FuncGraph('tmp').as_default():
    init_test = test()

# TensorFlow: Multiple evaluations are acceptable in this case, so we're fine
# with the re-evaluation of `test` that `_tf_while_stmt` will make.
if tensors.is_dense_tensor(init_test):
    _tf_while_stmt(test, body, get_state, set_state, symbol_names, opts)
    exit()

# Normal Python: We already consumed one evaluation of `test`; consistently,
# unroll one iteration before dispatching to a normal loop.
# TODO(mdan): Push the "init_test" value via opts into _py_while_stmt?
if not init_test:
    exit()
body()

_py_while_stmt(test, body, get_state, set_state, opts)
