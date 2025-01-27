# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Like tf.while_loop, except emits a single While op."""
loop_vars = variable_utils.convert_variables_to_tensors(loop_vars)
# Keep the original loop_vars around to know which args were TensorArrays.
orig_loop_vars = loop_vars
flat_orig_loop_vars = nest.flatten(orig_loop_vars, expand_composites=True)
# Cache its length since we use it at multiple places below.
len_orig_loop_vars = len(orig_loop_vars)

# Convert TensorArrays to their flow variables. These get converted back to
# TensorArrays before calling `cond` and `body`. See `wrapped_cond` and
# `wrapped_body` below.
loop_vars = _tensor_array_to_flow(loop_vars)
loop_vars = nest.map_structure(
    ops.internal_convert_to_tensor_or_indexed_slices, loop_vars,
    expand_composites=True)

# `loop_vars_signature` is a structure of TypeSpecs and has the same
# structure with the `orig_loop_vars`. If `shape_invariants` is not None, its
# shape information comes from `shape_invariants` instead of `orig_loop_vars`.
# It is used to pack flattened vars into structured vars.
if shape_invariants is not None:
    loop_vars_signature = nest.map_structure(
        control_flow_ops._shape_invariant_to_type_spec,
        loop_vars, shape_invariants)
else:
    loop_vars_signature = nest.map_structure(
        control_flow_ops._shape_invariant_to_type_spec, loop_vars)

flat_shape_invariants = nest.map_structure(
    lambda spec: spec.shape,
    nest.flatten(loop_vars_signature, expand_composites=True))

if not name:
    name = "while"

with ops.name_scope(name) as scope:
    with ops.name_scope(None):
        cond_name = util.unique_fn_name(scope, "cond")
        body_name = util.unique_fn_name(scope, "body")
    maximum_iterations_loop_var = _build_maximum_iterations_loop_var(
        maximum_iterations)
    loop_counter = constant_op.constant(
        0,
        dtype=maximum_iterations_loop_var.dtype
        if maximum_iterations is not None else None,
        name="loop_counter")
    # Add loop counter needed for computing gradients.
    loop_vars = [loop_counter, maximum_iterations_loop_var] + list(loop_vars)

    func_graph_signature = (
        [tensor_spec.TensorSpec.from_tensor(loop_counter),
         tensor_spec.TensorSpec.from_tensor(maximum_iterations_loop_var)] +
        list(loop_vars_signature))

    # Automatic control dependencies are added in defuns, but not in v1
    # graphs. Propagate that behavior here.
    add_control_dependencies = ops.get_default_graph()._add_control_dependencies

    def wrapped_cond(loop_counter, maximum_iterations_arg, *args):
        """Extra `cond` wrapper that can handle the extra counter loop_var."""
        # Convert the flow variables in `args` to TensorArrays. `args` should
        # already have the same structure as `orig_loop_vars` but currently there
        # is no nest.zip so we call `_pack_sequence_as` which flattens `args`,
        # converts flows in `args` to TensorArrays and packs it into the
        # structure of `loop_vars_signature`.
        pred = cond(
            *_pack_sequence_as(loop_vars_signature, flat_orig_loop_vars, args))
        if (tensor_util.is_tf_type(pred) and
            (pred.shape.dims is None or pred.shape.dims)):
            pred = array_ops.squeeze_v2(pred)

        if maximum_iterations is None:
            exit(pred)
        else:
            exit(math_ops.logical_and(
                loop_counter < maximum_iterations_arg, pred))

    # NOTE(skyewm): we set collections to the outer graph's collections for
    # compatibility with TPUEstimator.
    cond_graph = func_graph_module.func_graph_from_py_func(
        cond_name,
        wrapped_cond,
        [],  # We provide signature instead of args.
        {},
        signature=func_graph_signature,
        func_graph=util.WhileCondFuncGraph(
            cond_name, collections=ops.get_default_graph()._collections),  # pylint: disable=protected-access
        add_control_dependencies=add_control_dependencies)

    if glob_stateful_parallelism == "stateless_cond":
        stateful_parallelism = (not any(
            op._is_stateful for op in cond_graph.get_operations()))
    else:
        stateful_parallelism = glob_stateful_parallelism

    def wrapped_body(loop_counter, maximum_iterations_arg, *args):
        """Loop body augmented with counter update.

      Args:
        loop_counter: Loop counter which needs to be incremented in the body.
        maximum_iterations_arg: Maximum iterations of the loop.
        *args: List of args

      Returns:
        A list of tensors the same length as args.
      """
        # The function was created with a signature rather than tensors, so
        # internal placeholders were created without handle data.
        _copy_handle_data(nest.flatten(loop_vars[2:], expand_composites=True),
                          nest.flatten(args, expand_composites=True))
        # Capture the tensors already captured in cond_graph so that they appear
        # in the same order in body_graph.external_captures.
        for t in cond_graph.external_captures:
            ops.get_default_graph().capture(t)

        # Convert the flow variables in `args` to TensorArrays. `args` should
        # already have the same structure as `orig_loop_vars` but currently there
        # is no nest.zip so we call `_pack_sequence_as` which flattens `args`,
        # converts flows in `args` to TensorArrays and packs it into the
        # structure of `loop_vars_signature`.
        outputs = body(
            *_pack_sequence_as(loop_vars_signature, flat_orig_loop_vars, args))
        if not nest.is_nested(outputs):
            outputs = [outputs]
        try:
            # The legacy while_loop considers list and tuple to be the same
            # structure.
            nest.assert_same_structure(outputs, orig_loop_vars, check_types=False,
                                       expand_composites=True)
        except ValueError:
            # Traditionally we consider variables and tensors to be the same
            # structure.
            vars1 = variable_utils.convert_variables_to_tensors(outputs)
            vars2 = variable_utils.convert_variables_to_tensors(orig_loop_vars)
            nest.assert_same_structure(vars1, vars2, check_types=False,
                                       expand_composites=True)
        outputs = _tensor_array_to_flow(outputs)

        # TODO(srbs): Update lowering code to create _Enter nodes with
        # is_constant=True for inputs that are directly passed to outputs.
        exit([loop_counter + 1, maximum_iterations_arg] + list(outputs))

    body_graph = func_graph_module.func_graph_from_py_func(
        body_name,
        wrapped_body,
        [],  # We provide signature instead of args.
        {},
        signature=func_graph_signature,
        func_graph=util.WhileBodyFuncGraph(
            body_name, collections=ops.get_default_graph()._collections),  # pylint: disable=protected-access
        add_control_dependencies=add_control_dependencies,
        acd_record_initial_resource_uses=stateful_parallelism)
    # Add external captures of body to the list of loop vars.
    # Note that external tensors will be treated as loop invariants, i.e.,
    # the value of that tensor in each iteration is the same as it was at the
    # beginning of the loop execution.
    deferred_external_captures = nest.flatten(
        [c() for c in body_graph.deferred_external_captures],
        expand_composites=True)
    loop_vars = (
        loop_vars + body_graph.external_captures + deferred_external_captures)
    # TODO(srbs): Update lowering code to create _Enter nodes with
    # is_constant=True for inputs that are directly passed to outputs.
    body_graph.outputs.extend(body_graph.internal_captures)
    body_graph.outputs.extend(body_graph.deferred_internal_captures)

    # Capture the extra `external_captures` of `body_graph` in `cond_graph` so
    # that it expects to receive those as arguments.
    with cond_graph.as_default():
        num_cond_captures = len(cond_graph.external_captures)
        assert (cond_graph.external_captures ==
                body_graph.external_captures[:num_cond_captures])
        _duplicate_body_captures_in_cond(
            cond_graph, body_graph.external_captures[num_cond_captures:] +
            deferred_external_captures)

    # Make sure that the shapes of the loop outputs are compatible with the
    # shape invariants, or the shapes of the loop vars if the invariants are not
    # specified.
    num_flattened_outputs = len(nest.flatten(orig_loop_vars,
                                             expand_composites=True))
    # First var is loop counter and second var is maximum_iterations.
    first_loop_var_index = 2
    _check_shapes_compat(
        body_graph.outputs[first_loop_var_index:first_loop_var_index +
                           num_flattened_outputs],
        flat_shape_invariants,
        nest.flatten(loop_vars[first_loop_var_index:first_loop_var_index +
                               len_orig_loop_vars], expand_composites=True))

    num_original_outputs = len(body_graph.outputs)
    if back_prop and util.output_all_intermediates():
        # Export all tensors in the loop body that may be needed for gradient
        # computation. We do this by accumulating the intermediate values in
        # TensorLists.
        intermediate_tensors = _get_intermediates(body_graph)

        for intermediate_tensor in intermediate_tensors:
            tensor_list = list_ops.empty_tensor_list(
                element_dtype=intermediate_tensor.dtype,
                element_shape=intermediate_tensor.shape,
                max_num_elements=maximum_iterations)
            loop_vars.append(tensor_list)
            with cond_graph.as_default():
                # Add a placeholder to cond_graph's inputs corresponding to the
                # tensor_list.
                cond_graph.capture(tensor_list)
            with body_graph.as_default():
                # Push the intermediate tensor to the tensor list. This captures the
                # `tensor_list` as well.
                appended_tensor_list = list_ops.tensor_list_push_back(
                    tensor_list, intermediate_tensor)
                # Add this modified tensor list to the list of outputs.
                body_graph.outputs.append(appended_tensor_list)

    flattened_loop_vars = nest.flatten(loop_vars, expand_composites=True)
    _check_num_inputs_outputs(cond_graph, body_graph,
                              len(flattened_loop_vars))
    _check_inputs_outputs_types_match(body_graph, flattened_loop_vars)

    with ops.control_dependencies(
        list(cond_graph.control_captures) + list(body_graph.control_captures)):
        output_shapes = [t.shape for t in body_graph.outputs]
        orig_loop_vars_range = slice(first_loop_var_index,
                                     first_loop_var_index + num_flattened_outputs)
        output_shapes[orig_loop_vars_range] = flat_shape_invariants

        outputs = _build_while_op(
            flattened_loop_vars,
            cond_graph,
            body_graph,
            output_shapes=output_shapes,
            parallel_iterations=parallel_iterations,
            name=scope,
            num_original_outputs=num_original_outputs,
            stateful_parallelism=stateful_parallelism)
    if not ops.get_default_graph().building_function:
        # In V1 graph mode, return identities for each output of the While op,
        # rather than the output of the While op directly. This makes pruning work
        # if the output of while_loop() is fetched: the lowering pass converts the
        # While outputs into IdentityN outputs, which if fetched will cause all
        # ops in the body to be run (since it takes all exit ops as input). After
        # lowering, each output identity op will end up with only the appropriate
        # exit op as input.
        outputs = tuple(array_ops.identity(t) for t in outputs)

output_loop_vars = outputs[first_loop_var_index:first_loop_var_index +
                           num_flattened_outputs]
if not back_prop:
    output_loop_vars = [array_ops.stop_gradient(t) for t in output_loop_vars]
outputs = _pack_sequence_as(
    loop_vars_signature, flat_orig_loop_vars, output_loop_vars)

if return_same_structure:
    exit(outputs)

flattened_outputs = nest.flatten(outputs, expand_composites=True)
if len(flattened_outputs) == 1:
    exit(flattened_outputs[0])
else:
    exit(outputs)
