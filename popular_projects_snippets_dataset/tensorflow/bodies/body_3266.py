# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/save_model.py
"""Saves the model.

  Saves the provided graph def as SavedModel.
  Uses TF1 SavedModel semantics (i.e. no object graph).

  Args:
    graph_def: Graph to save.
    output_dir: Output directory for the SavedModel.
    signature_def_map: Mapping of signature def key -> SignatureDef.
    tags: Tags for the meta graph def.
    init_op_name: Name of the node for initialization.
    restore_op_name: Name of the node for restoration.
    checkpoint_dir: Path to checkpoint file where variable values are saved.
    variable_shared_names: Shared name of the variables in the model.

  Raises:
    ValueError iff the graph does not contain a valid signature.
  """
_create_empty_output_dir(output_dir)
v1_builder = builder.SavedModelBuilder(output_dir)

graph_def = _restore_output_tensor_names(graph_def)
with session.Session(graph=ops.Graph()) as sess:
    importer.import_graph_def(graph_def, name='')

    signature_def_map = _validate_signatures(
        signature_def_map, ops.get_default_graph()
    )

    # `restore_op_name` is non-empty & non-None when variables should be
    # restored before saving.
    if restore_op_name:
        var_mapping = _find_variables(graph_def)
        logging.debug(
            'Shared names of the variables to be saved: %s',
            str(list(var_mapping.keys())),
        )

        for shared_name in variable_shared_names:
            var_node_def = var_mapping[shared_name]

            # Variables with unknown shape and empty value is created. This is
            # just there to register a variable with `shared_name` to the resource
            # manager and collections, so that the values in checkpoint is
            # properly restored via `RestoreV2` op. Once restored, the value,
            # dtype and shape will be properly populated.
            _create_empty_variable(var_node_def)

        # Restores the variables by running the `RestoreV2` op.
        # `v1_builder.save()` saves the restored variables to the variables/
        # directory in `output_dir`.
        sess.run(
            _find_op(sess.graph, op_name=restore_op_name),
            feed_dict={_find_file_prefix_tensor(sess.graph): checkpoint_dir},
        )

    v1_builder.add_meta_graph_and_variables(
        sess,
        tags,
        signature_def_map=signature_def_map,
        main_op=_find_op(sess.graph, op_name=init_op_name),
    )

v1_builder.save()
