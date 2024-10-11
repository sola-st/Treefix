# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
if node.op in _CONTROL_FLOW_OPS:
    node.attr["_lower_using_switch_merge"].b = False
