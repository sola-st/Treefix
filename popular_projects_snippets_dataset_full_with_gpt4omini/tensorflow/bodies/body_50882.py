# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_serialization.py
"""Serialize a FunctionSpec object into its proto representation."""
if function_spec.is_method and not function_spec.fullargspec.args:
    raise NotImplementedError(
        "Cannot serialize a method function without a named "
        "'self' argument.")
proto = saved_object_graph_pb2.FunctionSpec()

# Intentionally skip encoding annotations of a function because function
# annotations are mainly for optional type checking during development
# and does not affect runtime behavior.
# https://www.python.org/dev/peps/pep-3107/
# https://docs.python.org/3/library/inspect.html#inspect.getfullargspec
proto.fullargspec.CopyFrom(
    nested_structure_coder.encode_structure(
        function_spec.fullargspec._replace(annotations={})))

proto.is_method = function_spec.is_method
proto.input_signature.CopyFrom(
    nested_structure_coder.encode_structure(function_spec.input_signature))

# See `tf.function` and the JitCompile proto for details.
proto.jit_compile = {
    None: saved_object_graph_pb2.FunctionSpec.JitCompile.DEFAULT,
    True: saved_object_graph_pb2.FunctionSpec.JitCompile.ON,
    False: saved_object_graph_pb2.FunctionSpec.JitCompile.OFF,
}.get(function_spec.jit_compile)

exit(proto)
