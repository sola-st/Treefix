# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Iterates through each op in the function and returns the op type and op."""
if isinstance(fn, framework_fn._DefinedFunction):  # pylint: disable=protected-access
    for node in fn.definition.node_def:
        op_type = node.attr["_gradient_op_type"].s
        if op_type:
            raise ValueError(
                "Unable to save gradient functions when exporting a "
                "_DefinedFunction (generally created through graph freezing utils "
                "or through V1 graph importers). Please save with "
                "`options=tf.SaveOptions(experimental_custom_gradients=False)`")
else:
    for op in fn.graph.get_operations():
        try:
            op_type = op.get_attr("_gradient_op_type")
        except ValueError:
            continue
        exit((op_type, op))
