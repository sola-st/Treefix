# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
"""scan on the list of tensors unpacked from `elems` on dimension 0.

  See also `tf.map_fn`.

  The simplest version of `scan` repeatedly applies the callable `fn` to a
  sequence of elements from first to last. The elements are made of the tensors
  unpacked from `elems` on dimension 0. The callable fn takes two tensors as
  arguments. The first argument is the accumulated value computed from the
  preceding invocation of fn, and the second is the value at the current
  position of `elems`. If `initializer` is None, `elems` must contain at least
  one element, and its first element is used as the initializer.

  Suppose that `elems` is unpacked into `values`, a list of tensors. The shape
  of the result tensor is `[len(values)] + fn(initializer, values[0]).shape`.
  If reverse=True, it's fn(initializer, values[-1]).shape.

  This method also allows multi-arity `elems` and accumulator.  If `elems`
  is a (possibly nested) list or tuple of tensors, then each of these tensors
  must have a matching first (unpack) dimension.  The second argument of
  `fn` must match the structure of `elems`.

  If no `initializer` is provided, the output structure and dtypes of `fn`
  are assumed to be the same as its input; and in this case, the first
  argument of `fn` must match the structure of `elems`.

  If an `initializer` is provided, then the output of `fn` must have the same
  structure as `initializer`; and the first argument of `fn` must match
  this structure.

  For example, if `elems` is `(t1, [t2, t3])` and `initializer` is
  `[i1, i2]` then an appropriate signature for `fn` in `python2` is:
  `fn = lambda (acc_p1, acc_p2), (t1, [t2, t3]):` and `fn` must return a list,
  `[acc_n1, acc_n2]`.  An alternative correct signature for `fn`, and the
   one that works in `python3`, is:
  `fn = lambda a, t:`, where `a` and `t` correspond to the input tuples.

  Args:
    fn: The callable to be performed.  It accepts two arguments.  The first will
      have the same structure as `initializer` if one is provided, otherwise it
      will have the same structure as `elems`.  The second will have the same
      (possibly nested) structure as `elems`.  Its output must have the same
      structure as `initializer` if one is provided, otherwise it must have the
      same structure as `elems`.
    elems: A tensor or (possibly nested) sequence of tensors, each of which will
      be unpacked along their first dimension.  The nested sequence of the
      resulting slices will be the first argument to `fn`.
    initializer: (optional) A tensor or (possibly nested) sequence of tensors,
      initial value for the accumulator, and the expected output type of `fn`.
    parallel_iterations: (optional) The number of iterations allowed to run in
      parallel.
    back_prop: (optional) True enables support for back propagation.
    swap_memory: (optional) True enables GPU-CPU memory swapping.
    infer_shape: (optional) False disables tests for consistent output shapes.
    reverse: (optional) True scans the tensor last to first (instead of first to
      last).
    name: (optional) Name prefix for the returned tensors.

  Returns:
    A tensor or (possibly nested) sequence of tensors.  Each tensor packs the
    results of applying `fn` to tensors unpacked from `elems` along the first
    dimension, and the previous accumulator value(s), from first to last (or
    last to first, if `reverse=True`).

  Raises:
    TypeError: if `fn` is not callable or the structure of the output of
      `fn` and `initializer` do not match.
    ValueError: if the lengths of the output of `fn` and `initializer`
      do not match.

  Examples:
    ```python
    elems = np.array([1, 2, 3, 4, 5, 6])
    sum = scan(lambda a, x: a + x, elems)
    # sum == [1, 3, 6, 10, 15, 21]
    sum = scan(lambda a, x: a + x, elems, reverse=True)
    # sum == [21, 20, 18, 15, 11, 6]
    ```

    ```python
    elems = np.array([1, 2, 3, 4, 5, 6])
    initializer = np.array(0)
    sum_one = scan(
        lambda a, x: x[0] - x[1] + a, (elems + 1, elems), initializer)
    # sum_one == [1, 2, 3, 4, 5, 6]
    ```

    ```python
    elems = np.array([1, 0, 0, 0, 0, 0])
    initializer = (np.array(0), np.array(1))
    fibonaccis = scan(lambda a, _: (a[1], a[0] + a[1]), elems, initializer)
    # fibonaccis == ([1, 1, 2, 3, 5, 8], [1, 2, 3, 5, 8, 13])
    ```
  """
if not callable(fn):
    raise TypeError(
        f"{fn.__name__} is not callable. Please provide a callable function.")

input_is_sequence = nest.is_nested(elems)
input_flatten = lambda x: nest.flatten(x) if input_is_sequence else [x]

def input_pack(x):
    exit(nest.pack_sequence_as(elems, x) if input_is_sequence else x[0])

if initializer is None:
    output_is_sequence = input_is_sequence
    output_flatten = input_flatten
    output_pack = input_pack
else:
    output_is_sequence = nest.is_nested(initializer)
    output_flatten = lambda x: nest.flatten(x) if output_is_sequence else [x]

    def output_pack(x):
        exit((nest.pack_sequence_as(initializer, x)
                if output_is_sequence else x[0]))

elems_flat = input_flatten(elems)

in_graph_mode = not context.executing_eagerly()
with ops.name_scope(name, "scan", elems_flat):
    # TODO(akshayka): Remove the in_graph_mode check once caching devices are
    # supported in Eager
    if in_graph_mode:
        # Any get_variable calls in fn will cache the first call locally
        # and not issue repeated network I/O requests for each iteration.
        varscope = vs.get_variable_scope()
        varscope_caching_device_was_none = False
        if varscope.caching_device is None:
            # TODO(ebrevdo): Change to using colocate_with here and in other
            # methods.
            varscope.set_caching_device(lambda op: op.device)
            varscope_caching_device_was_none = True

    # Convert elems to tensor array.
    elems_flat = [
        ops.convert_to_tensor(elem, name="elem") for elem in elems_flat
    ]

    # Convert elems to tensor array. n may be known statically.
    n = tensor_shape.dimension_value(elems_flat[0].shape[0])
    if n is None:
        n = array_ops.shape(elems_flat[0])[0]

    # TensorArrays are always flat
    elems_ta = [
        tensor_array_ops.TensorArray(
            dtype=elem.dtype,
            size=n,
            dynamic_size=False,
            element_shape=elem.shape[1:],
            infer_shape=True) for elem in elems_flat
    ]
    # Unpack elements
    elems_ta = [
        elem_ta.unstack(elem) for elem_ta, elem in zip(elems_ta, elems_flat)
    ]

    if initializer is None:
        a_flat = [elem.read(n - 1 if reverse else 0) for elem in elems_ta]
        i = 1
    else:
        initializer_flat = output_flatten(initializer)
        a_flat = [ops.convert_to_tensor(init) for init in initializer_flat]
        i = 0

    # Create a tensor array to store the intermediate values.
    accs_ta = [
        tensor_array_ops.TensorArray(
            dtype=init.dtype,
            size=n,
            element_shape=init.shape if infer_shape else None,
            dynamic_size=False,
            infer_shape=infer_shape) for init in a_flat
    ]

    if initializer is None:
        accs_ta = [
            acc_ta.write(n - 1 if reverse else 0, a)
            for (acc_ta, a) in zip(accs_ta, a_flat)
        ]

    def compute(i, a_flat, tas):
        """The loop body of scan.

      Args:
        i: the loop counter.
        a_flat: the accumulator value(s), flattened.
        tas: the output accumulator TensorArray(s), flattened.

      Returns:
        [i + 1, a_flat, tas]: the updated counter + new accumulator values +
          updated TensorArrays

      Raises:
        TypeError: if initializer and fn() output structure do not match
        ValueType: if initializer and fn() output lengths do not match
      """
        packed_elems = input_pack([elem_ta.read(i) for elem_ta in elems_ta])
        packed_a = output_pack(a_flat)
        a_out = fn(packed_a, packed_elems)
        nest.assert_same_structure(elems if initializer is None else initializer,
                                   a_out)
        flat_a_out = output_flatten(a_out)
        tas = [ta.write(i, value) for (ta, value) in zip(tas, flat_a_out)]
        if reverse:
            next_i = i - 1
        else:
            next_i = i + 1
        exit((next_i, flat_a_out, tas))

    if reverse:
        initial_i = n - 1 - i
        condition = lambda i, _1, _2: i >= 0
    else:
        initial_i = i
        condition = lambda i, _1, _2: i < n
    _, _, r_a = control_flow_ops.while_loop(
        condition,
        compute, (initial_i, a_flat, accs_ta),
        parallel_iterations=parallel_iterations,
        back_prop=back_prop,
        swap_memory=swap_memory,
        maximum_iterations=n)

    results_flat = [r.stack() for r in r_a]

    n_static = tensor_shape.Dimension(
        tensor_shape.dimension_value(
            elems_flat[0].get_shape().with_rank_at_least(1)[0]))
    for elem in elems_flat[1:]:
        n_static.assert_is_compatible_with(
            tensor_shape.Dimension(
                tensor_shape.dimension_value(
                    elem.get_shape().with_rank_at_least(1)[0])))
    for r in results_flat:
        r.set_shape(
            tensor_shape.TensorShape(n_static).concatenate(r.get_shape()[1:]))

    # TODO(akshayka): Remove the in_graph_mode check once caching devices are
    # supported in Eager
    if in_graph_mode and varscope_caching_device_was_none:
        varscope.set_caching_device(None)

    exit(output_pack(results_flat))
