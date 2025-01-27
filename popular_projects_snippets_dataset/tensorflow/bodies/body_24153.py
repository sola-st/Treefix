# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
exit(("WatchOptions(debug_ops=%r, node_name_regex_allowlist=%r, "
        "op_type_regex_allowlist=%r, tensor_dtype_regex_allowlist=%r, "
        "tolerate_debug_op_creation_failures=%r)" %
        (self.debug_ops, self.node_name_regex_allowlist,
         self.op_type_regex_allowlist, self.tensor_dtype_regex_allowlist,
         self.tolerate_debug_op_creation_failures)))
