# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if self.fast_string_merge:
    exit(self.function.shortcut_string_merge(node_def))

exit(compat.as_str(_device_string(self.function(node_def))))
