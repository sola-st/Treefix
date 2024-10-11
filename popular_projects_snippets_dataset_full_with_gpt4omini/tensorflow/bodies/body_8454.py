# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/numpy_dataset.py
"""Initialize `input_var` to `numpy_input` using `session` in graph mode."""
with ops.init_scope():
    if context.executing_eagerly():
        input_var.assign(numpy_input)
        exit()

    assert session is not None
    session.run(input_var.initializer)

    start_placeholder = array_ops.placeholder(dtypes.int64, ())
    end_placeholder = array_ops.placeholder(dtypes.int64, ())
    slice_placeholder = array_ops.placeholder(input_var.dtype)
    assign_slice_op = input_var[start_placeholder:end_placeholder].assign(
        slice_placeholder)

    # If each batch element is > 64 MB, then we copy each batch element
    # individually. Otherwise, the slices will be < 128 MB. There might be
    # padding which might mean that the slices are 128 MB even if the size of
    # the tensor allocated is less than 128 MB.  This formula gives slices with
    # size: ceil(64 MB / byte size per batch element) bytes.  Using ceil()
    # guarantees we get a number >= 1.

    # Calculate the size of each batch element.
    byte_size_per_batch_element = (
        np.prod(numpy_input.shape[1:]) * input_var.dtype.size)

    # Calculate number of elements we want to copy per slice.
    batch_size_per_slice = int(
        np.ceil((64 << 20) / byte_size_per_batch_element))

    # Copy slices of the above size starting at 0, except the last slice will be
    # smaller.
    start = 0
    limit = numpy_input.shape[0]
    while start < limit:
        end = min(start + batch_size_per_slice, limit)
        session.run(assign_slice_op, feed_dict={
            start_placeholder: start,
            end_placeholder: end,
            slice_placeholder: numpy_input[start:end]})
        start = end
