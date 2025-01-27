# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/freeze_graph.py
if flags.checkpoint_version == 1:
    checkpoint_version = saver_pb2.SaverDef.V1
elif flags.checkpoint_version == 2:
    checkpoint_version = saver_pb2.SaverDef.V2
else:
    raise ValueError("Invalid checkpoint version (must be '1' or '2'): %d" %
                     flags.checkpoint_version)
freeze_graph(flags.input_graph, flags.input_saver, flags.input_binary,
             flags.input_checkpoint, flags.output_node_names,
             flags.restore_op_name, flags.filename_tensor_name,
             flags.output_graph, flags.clear_devices, flags.initializer_nodes,
             flags.variable_names_whitelist, flags.variable_names_denylist,
             flags.input_meta_graph, flags.input_saved_model_dir,
             flags.saved_model_tags, checkpoint_version)
