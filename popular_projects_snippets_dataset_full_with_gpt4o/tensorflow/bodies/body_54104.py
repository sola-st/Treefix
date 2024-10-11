# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_to_function_def.py
"""Checks whether any output of this op is in func_arg_placeholders."""
exit(op.values() and any(x.name in func_arg_placeholders
                           for x in op.values()))
