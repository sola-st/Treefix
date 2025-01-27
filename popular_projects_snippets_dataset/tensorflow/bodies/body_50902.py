# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Deserialize a FunctionSpec object from its proto representation."""
typeless_fullargspec = nested_structure_coder.decode_proto(
    function_spec_proto.fullargspec)

# Convert a method function into a non method.
if function_spec_proto.is_method:
    if not typeless_fullargspec.args:
        raise NotImplementedError(
            "Cannot deserialize a method function without a named "
            "'self' argument.")
    args = typeless_fullargspec.args[1:]
else:
    args = typeless_fullargspec.args

fullargspec = tf_inspect.FullArgSpec(
    args=args,
    varargs=typeless_fullargspec.varargs,
    varkw=typeless_fullargspec.varkw,
    defaults=typeless_fullargspec.defaults,
    kwonlyargs=typeless_fullargspec.kwonlyargs,
    kwonlydefaults=typeless_fullargspec.kwonlydefaults,
    annotations=typeless_fullargspec.annotations)
input_signature = nested_structure_coder.decode_proto(
    function_spec_proto.input_signature)

# See `tf.function` and the JitCompile proto for details.
jit_compile = {
    saved_object_graph_pb2.FunctionSpec.JitCompile.DEFAULT: None,
    saved_object_graph_pb2.FunctionSpec.JitCompile.ON: True,
    saved_object_graph_pb2.FunctionSpec.JitCompile.OFF: False,
}.get(function_spec_proto.jit_compile)

exit(function_spec_lib.FunctionSpec.from_fullargspec_and_signature(
    fullargspec=fullargspec,
    is_bound_method=False,
    input_signature=input_signature,
    jit_compile=jit_compile))
