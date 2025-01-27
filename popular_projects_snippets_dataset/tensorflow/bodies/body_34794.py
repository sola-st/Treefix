# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
saver.import_meta_graph(meta_graph)
exit(ops.get_default_graph().get_tensor_by_name(op.name))
