# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
exit(dict(
    (_tensor_name_base(node.name), idx) for idx, node in enumerate(nodes)))
