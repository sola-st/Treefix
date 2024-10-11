# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2.py
"""Creates ConcreteFunctions for signatures in `meta_graph_def`."""
signature_functions = {}
for signature_key, signature_def in meta_graph_def.signature_def.items():
    if signature_def.inputs:
        input_items = sorted(
            signature_def.inputs.items(), key=lambda item: item[0])
        original_input_names, input_specs = zip(*input_items)
    else:
        original_input_names = []
        input_specs = []
    # TODO(b/205015292): Support optional arguments
    feeds = [
        wrap_function._get_element_from_tensor_info(input_spec, wrapped.graph)  # pylint: disable=protected-access
        for input_spec in input_specs
    ]
    input_names = []
    input_tensors = []
    for original_input_name, feed in zip(original_input_names, feeds):
        if isinstance(feed, sparse_tensor.SparseTensor):
            # We have to give explicit name for SparseTensor arguments, because
            # these are not present in the TensorInfo.
            indices_name = "%s_indices" % original_input_name
            values_name = "%s_values" % original_input_name
            dense_shape_name = "%s_dense_shape" % original_input_name
            input_names.extend([indices_name, values_name, dense_shape_name])
            input_tensors.extend([feed.indices, feed.values, feed.dense_shape])
        elif isinstance(feed, composite_tensor.CompositeTensor):
            component_tensors = nest.flatten(feed, expand_composites=True)
            input_names.extend("%s_component_%d" % (original_input_name, n)
                               for n in range(len(component_tensors)))
            input_tensors.extend(component_tensors)
        else:
            input_names.append(original_input_name)
            input_tensors.append(feed)
    fetches = {name: out for name, out in signature_def.outputs.items()}
    try:
        signature_fn = wrapped.prune(feeds=feeds, fetches=fetches)
    except lift_to_graph.UnliftableError as ex:
        # Mutate the exception to add a bit more detail.
        args = ex.args
        if not args:
            message = ""
        else:
            message = args[0]
        message = (
            ("A SavedModel signature needs an input for each placeholder the "
             "signature's outputs use. An output for signature '{}' depends on "
             "a placeholder which is not an input (i.e. the placeholder is not "
             "fed a value).\n\n").format(signature_key)
            + message)
        ex.args = (message,) + args[1:]
        raise
    # pylint: disable=protected-access
    signature_fn._arg_keywords = input_names
    signature_fn._func_graph.structured_input_signature = (
        (),
        func_graph.convert_structure_to_signature(
            dict(zip(input_names, input_tensors))))

    if len(input_names) == 1:
        # Allowing positional arguments does not create any ambiguity if there's
        # only one.
        signature_fn._num_positional_args = 1
    else:
        signature_fn._num_positional_args = 0
    # pylint: enable=protected-access
    signature_functions[signature_key] = signature_fn
exit(signature_functions)
