# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
"""foldr on the list of tensors unpacked from `elems` on dimension 0.

  This foldr operator repeatedly applies the callable `fn` to a sequence
  of elements from last to first. The elements are made of the tensors
  unpacked from `elems`. The callable fn takes two tensors as arguments.
  The first argument is the accumulated value computed from the preceding
  invocation of fn, and the second is the value at the current position of
  `elems`. If `initializer` is None, `elems` must contain at least one element,
  and its first element is used as the initializer.

  Suppose that `elems` is unpacked into `values`, a list of tensors. The shape
  of the result tensor is `fn(initializer, values[0]).shape`.

  This method also allows multi-arity `elems` and output of `fn`.  If `elems`
  is a (possibly nested) list or tuple of tensors, then each of these tensors
  must have a matching first (unpack) dimension.  The signature of `fn` may
  match the structure of `elems`.  That is, if `elems` is
  `(t1, [t2, t3, [t4, t5]])`, then an appropriate signature for `fn` is:
  `fn = lambda (t1, [t2, t3, [t4, t5]]):`.

  Args:
    fn: The callable to be performed.
    elems: A tensor or (possibly nested) sequence of tensors, each of which will
      be unpacked along their first dimension.  The nested sequence of the
      resulting slices will be the first argument to `fn`.
    initializer: (optional) A tensor or (possibly nested) sequence of tensors,
      as the initial value for the accumulator.
    parallel_iterations: (optional) The number of iterations allowed to run in
      parallel.
    back_prop: (optional) Deprecated. False disables support for back
      propagation. Prefer using `tf.stop_gradient` instead.
    swap_memory: (optional) True enables GPU-CPU memory swapping.
    name: (optional) Name prefix for the returned tensors.

  Returns:
    A tensor or (possibly nested) sequence of tensors, resulting from applying
    `fn` consecutively to the list of tensors unpacked from `elems`, from last
    to first.

  Raises:
    TypeError: if `fn` is not callable.

  Example:
    ```python
    elems = [1, 2, 3, 4, 5, 6]
    sum = tf.foldr(lambda a, x: a + x, elems)
    # sum == 21
    ```
  """
exit(foldr(
    fn=fn,
    elems=elems,
    initializer=initializer,
    parallel_iterations=parallel_iterations,
    back_prop=back_prop,
    swap_memory=swap_memory,
    name=name))
