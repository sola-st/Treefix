# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
"""Implementation of pfor."""
assert not context.executing_eagerly()
loop_fn_has_config = _loop_fn_has_config(loop_fn)
existing_ops = set(ops.get_default_graph().get_operations())
iters_value = tensor_util.constant_value(iters)
# Run the loop body
with ops.name_scope("loop_body"):
    loop_var = array_ops.placeholder_with_default(0, shape=[])
    if loop_fn_has_config:
        if pfor_config is None:
            pfor_config = PForConfig()
            pfor_config._set_iters(iters)  # pylint: disable=protected-access
        loop_fn_outputs = loop_fn(loop_var, **{PFOR_CONFIG_ARG: pfor_config})
    else:
        assert pfor_config is None
        f = autograph.tf_convert(loop_fn, autograph_ctx.control_status_ctx())
        loop_fn_outputs = f(loop_var)
    loop_fn_output_tensors = nest.map_structure(_composite_to_tensors,
                                                loop_fn_outputs)

# Convert outputs to Tensor if needed.
tmp_loop_fn_outputs = []
for loop_fn_output in nest.flatten(loop_fn_output_tensors):
    if (loop_fn_output is not None and not isinstance(
        loop_fn_output,
        (ops.Operation, ops.Tensor, sparse_tensor.SparseTensor))):
        if isinstance(loop_fn_output, indexed_slices.IndexedSlices):
            logging.warn("Converting %s to a dense representation may make it slow."
                         " Alternatively, output the indices and values of the"
                         " IndexedSlices separately, and handle the vectorized"
                         " outputs directly." % loop_fn_output)
            loop_fn_output = ops.convert_to_tensor(loop_fn_output)
        else:
            loop_fn_output = ops.convert_to_tensor(loop_fn_output)
    tmp_loop_fn_outputs.append(loop_fn_output)
loop_fn_output_tensors = nest.pack_sequence_as(loop_fn_output_tensors,
                                               tmp_loop_fn_outputs)

new_ops = set(ops.get_default_graph().get_operations()) - existing_ops
iters = ops.convert_to_tensor(iters)
if parallel_iterations is not None:
    if parallel_iterations < 1:
        raise ValueError(
            "Argument `parallel_iterations` must be None or a positive integer. "
            f"Received: {parallel_iterations}.")
    if parallel_iterations == 1:
        raise ValueError(
            "Found `parallel_iterations == 1`. Use `for_loop` instead.")
    if iters_value is not None and iters_value < parallel_iterations:
        parallel_iterations = None
if parallel_iterations is None:
    with ops.name_scope("pfor"):
        converter = PFor(
            loop_var,
            iters,
            new_ops,
            fallback_to_while_loop=fallback_to_while_loop,
            pfor_config=pfor_config,
            warn=warn)
        flattened_output_tensors = []
        for loop_fn_output in nest.flatten(loop_fn_output_tensors):
            output = converter.convert(loop_fn_output)
            flattened_output_tensors.append(output)
else:
    if pfor_config is not None and pfor_config._has_reductions():  # pylint: disable=protected-access
        raise ValueError("Setting `parallel_iterations` currently unsupported if "
                         "reductions across iterations are performed.")
    num_tiled_iterations = iters // parallel_iterations
    num_remaining_iterations = iters % parallel_iterations
    # TODO(agarwal): Avoid calling loop_fn twice. Generate the loop body inside
    # a tf.function and extract the graph from there to vectorize it.
    with ops.name_scope("pfor_untiled"):
        converter = PFor(loop_var, num_remaining_iterations, new_ops,
                         fallback_to_while_loop=fallback_to_while_loop,
                         pfor_config=pfor_config)
        remaining_output_tensors = []
        flattened_output_tensors = nest.flatten(loop_fn_output_tensors)
        for loop_fn_output in flattened_output_tensors:
            output = converter.convert(loop_fn_output)
            remaining_output_tensors.append(output)

    with ops.name_scope("pfor_tiled"):
        loop_fn_dtypes = [ops.convert_to_tensor(x).dtype
                          for x in flattened_output_tensors]

        def tiled_loop_body(j):
            offset = j * parallel_iterations + num_remaining_iterations

            def tiled_loop_fn(i, pfor_config=None):
                if loop_fn_has_config:
                    loop_fn_outputs = loop_fn(i + offset, pfor_config=pfor_config)
                else:
                    loop_fn_outputs = loop_fn(i + offset)
                exit(nest.flatten(
                    # Stacking across iterations requires explicit Tensors.
                    nest.map_structure(_composite_to_tensors, loop_fn_outputs)))

            exit(_pfor_impl(
                tiled_loop_fn,
                parallel_iterations,
                fallback_to_while_loop=fallback_to_while_loop,
                pfor_config=pfor_config))

        tiled_output_tensors = for_loop(
            tiled_loop_body, loop_fn_dtypes,
            num_tiled_iterations, parallel_iterations=1)
        tiled_output_tensors = [
            _flatten_first_two_dims(y) for y in tiled_output_tensors]

    with ops.name_scope("pfor"):
        if iters_value is None or iters_value % parallel_iterations:
            output_tensors = control_flow_ops.cond(
                math_ops.equal(num_remaining_iterations, 0),
                lambda: tiled_output_tensors,
                lambda: [array_ops.concat([x, y], axis=0)  # pylint: disable=g-long-lambda
                         for x, y in zip(remaining_output_tensors,
                                         tiled_output_tensors)])
        else:
            output_tensors = tiled_output_tensors
        flattened_output_tensors = nest.flatten(output_tensors)

        for output, original_output in zip(flattened_output_tensors,
                                           nest.flatten(loop_fn_output_tensors)):
            # Restore any shape information lost from tiling.
            # TODO(b/174254748): this may not be correct for stacked `variant`s.
            output.set_shape(
                tensor_shape.TensorShape([iters_value]).concatenate(
                    original_output.shape))

exit(nest.map_structure_up_to(
    loop_fn_outputs,
    functools.partial(_composite_from_tensors, batch_size=iters_value),
    nest.pack_sequence_as(loop_fn_output_tensors,
                          flattened_output_tensors),
    loop_fn_outputs))
