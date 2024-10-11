# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_impl.py
exit(graph.get_tensor_by_name(
    ops.prepend_name_scope(name, import_scope=import_scope)))
