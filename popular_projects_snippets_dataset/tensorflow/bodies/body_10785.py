# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Return `true_fn()` if the predicate `pred` is true else `false_fn()`.

  `true_fn` and `false_fn` both return lists of output tensors. `true_fn` and
  `false_fn` must have the same non-zero number and type of outputs.

  **WARNING**: Any Tensors or Operations created outside of `true_fn` and
  `false_fn` will be executed regardless of which branch is selected at runtime.

  Although this behavior is consistent with the dataflow model of TensorFlow,
  it has frequently surprised users who expected a lazier semantics.
  Consider the following simple program:

  ```python
  z = tf.multiply(a, b)
  result = tf.cond(x < y, lambda: tf.add(x, z), lambda: tf.square(y))
  ```

  If `x < y`, the `tf.add` operation will be executed and `tf.square`
  operation will not be executed. Since `z` is needed for at least one
  branch of the `cond`, the `tf.multiply` operation is always executed,
  unconditionally.

  Note that `cond` calls `true_fn` and `false_fn` *exactly once* (inside the
  call to `cond`, and not at all during `Session.run()`). `cond`
  stitches together the graph fragments created during the `true_fn` and
  `false_fn` calls with some additional graph nodes to ensure that the right
  branch gets executed depending on the value of `pred`.

  `tf.cond` supports nested structures as implemented in
  `tensorflow.python.util.nest`. Both `true_fn` and `false_fn` must return the
  same (possibly nested) value structure of lists, tuples, and/or named tuples.
  Singleton lists and tuples form the only exceptions to this: when returned by
  `true_fn` and/or `false_fn`, they are implicitly unpacked to single values.
  This behavior is disabled by passing `strict=True`.

  Args:
    pred: A scalar determining whether to return the result of `true_fn` or
      `false_fn`.
    true_fn: The callable to be performed if pred is true.
    false_fn: The callable to be performed if pred is false.
    strict: A boolean that enables/disables 'strict' mode; see above.
    name: Optional name prefix for the returned tensors.

  Returns:
    Tensors returned by the call to either `true_fn` or `false_fn`. If the
    callables return a singleton list, the element is extracted from the list.

  Raises:
    TypeError: if `true_fn` or `false_fn` is not callable.
    ValueError: if `true_fn` and `false_fn` do not return the same number of
      tensors, or return tensors of different types.

  Example:

  ```python
  x = tf.constant(2)
  y = tf.constant(5)
  def f1(): return tf.multiply(x, 17)
  def f2(): return tf.add(y, 23)
  r = tf.cond(tf.less(x, y), f1, f2)
  # r is set to f1().
  # Operations in f2 (e.g., tf.add) are not executed.
  ```

  """
# We needed to make true_fn/false_fn keyword arguments for
# backwards-compatibility. This check exists so that we can convert back to
# having them be positional arguments.
# TODO(josh11b): Make `true_fn` and `false_fn` positional arguments after
# `fn1` and `fn2` are deleted.
if fn1 is not None:
    if true_fn is not None:
        raise TypeError(
            "cond(): 'true_fn' and 'fn1' may not be set simultaneously.")
    true_fn = fn1
elif true_fn is None:
    raise TypeError("cond(): 'true_fn' argument required")
if fn2 is not None:
    if false_fn is not None:
        raise TypeError(
            "cond(): 'false_fn' and 'fn2' may not be set simultaneously.")
    false_fn = fn2
elif false_fn is None:
    raise TypeError("cond(): 'false_fn' argument required")

if not callable(true_fn):
    raise TypeError("'true_fn' must be callable.")
if not callable(false_fn):
    raise TypeError("'false_fn' must be callable.")

if context.executing_eagerly():
    exit(_eager_cond_implementation(pred, true_fn, false_fn, strict, name))

# Always enable control flow v2 if building a function, regardless of toggle.
if util.EnableControlFlowV2(ops.get_default_graph()):
    exit(cond_v2.cond_v2(pred, true_fn, false_fn, name))

with ops.name_scope(name, "cond", [pred]):
    # Add the Switch to the graph.
    if isinstance(pred, bool):
        raise TypeError("'pred' must not be a Python bool.")
    p_2, p_1 = switch(pred, pred)
    pivot_1 = array_ops.identity(p_1, name="switch_t")
    pivot_2 = array_ops.identity(p_2, name="switch_f")
    pred = array_ops.identity(pred, name="pred_id")
    # Disable the fetching of tensors that are only on one branch of cond.
    for tensor in [p_1, p_2, pivot_1, pivot_2, pred]:
        tensor.op.graph.prevent_fetching(tensor.op)

    # Build the graph for the true branch in a new context.
    context_t = CondContext(pred, pivot_1, branch=1)
    try:
        context_t.Enter()
        orig_res_t, res_t = context_t.BuildCondBranch(true_fn)
        if orig_res_t is None:
            raise ValueError("'true_fn' must have a return value.")
        context_t.ExitResult(res_t)
    finally:
        context_t.Exit()

    # Build the graph for the false branch in a new context.
    context_f = CondContext(pred, pivot_2, branch=0)
    try:
        context_f.Enter()
        orig_res_f, res_f = context_f.BuildCondBranch(false_fn)
        if orig_res_f is None:
            raise ValueError("'false_fn' must have a return value.")
        context_f.ExitResult(res_f)
    finally:
        context_f.Exit()

    if not strict:
        orig_res_t = _UnpackIfSingleton(orig_res_t)
        orig_res_f = _UnpackIfSingleton(orig_res_f)

    # Check that the return values of the two branches have the same structure.
    try:
        nest.assert_same_structure(orig_res_t, orig_res_f, expand_composites=True)
    except (TypeError, ValueError):
        nest.map_structure(_cast_indexed_slice_indices, orig_res_t, orig_res_f)
        nest.map_structure(_cast_indexed_slice_indices, res_t, res_f)
        try:
            nest.assert_same_structure(orig_res_t, orig_res_f,
                                       expand_composites=True)
        except TypeError as e:
            raise TypeError(
                f"Incompatible return types of 'true_fn' and 'false_fn': {e}")
        except ValueError as e:
            raise ValueError(
                f"Incompatible return values of 'true_fn' and 'false_fn': {e}")

    # Add the final merge to the graph.
    if not res_t:
        raise ValueError(
            "'true_fn' and 'false_fn' must return at least one result.")

    res_t_flat = nest.flatten(res_t, expand_composites=True)
    res_f_flat = nest.flatten(res_f, expand_composites=True)

    for (x, y) in zip(res_t_flat, res_f_flat):
        assert isinstance(x, ops.Tensor) and isinstance(y, ops.Tensor)
        if x.dtype.base_dtype != y.dtype.base_dtype:
            raise ValueError(
                "Outputs of 'true_fn' and 'false_fn' must have the same type(s). "
                f"Received {x.dtype.name} from 'true_fn' "
                f"and {y.dtype.name} from 'false_fn'.")

    merges = [merge(pair)[0] for pair in zip(res_f_flat, res_t_flat)]
    merges = nest.map_structure(
        _convert_flow_to_tensorarray,
        nest.flatten(orig_res_t, expand_composites=True),
        merges)

    # Only add non-nested conds to the collection. Any nested control flow will
    # be encapsulated in the root context.
    assert context_t.outer_context == context_f.outer_context
    if context_t.outer_context is None:
        ops.add_to_collection(ops.GraphKeys.COND_CONTEXT, context_t)
        ops.add_to_collection(ops.GraphKeys.COND_CONTEXT, context_f)

    merges = nest.pack_sequence_as(
        structure=orig_res_t, flat_sequence=merges, expand_composites=True)

    # Singleton lists and tuples are automatically unpacked if strict == False.
    if not strict:
        merges = _UnpackIfSingleton(merges)
    exit(merges)
