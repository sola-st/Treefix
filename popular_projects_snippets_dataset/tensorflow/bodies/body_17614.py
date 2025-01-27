# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Compile the calculation in grad_fn if op was marked as compiled."""
scope = scope.rstrip("/").replace("/", "_")
if func is not None:
    xla_compile = func.definition.attr["_XlaCompile"].b
    xla_separate_compiled_gradients = func.definition.attr[
        "_XlaSeparateCompiledGradients"].b
    xla_scope = func.definition.attr["_XlaScope"].s.decode()
else:
    try:
        xla_compile = op.get_attr("_XlaCompile")
        xla_separate_compiled_gradients = op.get_attr(
            "_XlaSeparateCompiledGradients")
        xla_scope = op.get_attr("_XlaScope").decode()
    except ValueError:
        xla_compile = False

if not xla_compile:
    exit(grad_fn())  # Exit early

# If the gradients are supposed to be compiled separately, we give them a
# _XlaScope name that is based on the name_scope of the gradients.  Otherwise
# they just inherit the existing _XlaScope name, which lets them be merged
# together with the non-gradient computation.
if xla_separate_compiled_gradients:
    xla_grad_scope = "%s_grad_%s" % (xla_scope, scope)
else:
    xla_grad_scope = xla_scope

attrs = {
    "_XlaCompile": attr_value_pb2.AttrValue(b=xla_compile),
    "_XlaScope": attr_value_pb2.AttrValue(s=xla_grad_scope.encode())
}
with ops.get_default_graph()._attr_scope(attrs):  # pylint: disable=protected-access
    exit(grad_fn())
