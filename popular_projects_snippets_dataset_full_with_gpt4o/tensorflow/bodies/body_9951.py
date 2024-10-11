# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/strip_unused.py
strip_unused_lib.strip_unused_from_files(FLAGS.input_graph,
                                         FLAGS.input_binary,
                                         FLAGS.output_graph,
                                         FLAGS.output_binary,
                                         FLAGS.input_node_names,
                                         FLAGS.output_node_names,
                                         FLAGS.placeholder_type_enum)
