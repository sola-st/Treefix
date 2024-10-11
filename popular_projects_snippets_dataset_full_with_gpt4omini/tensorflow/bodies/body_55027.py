# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Function definition proto."""
self._create_definition_if_needed()
if self._c_func:
    with c_api_util.tf_buffer() as buf:
        with self._c_func.get() as func:
            c_api.TF_FunctionToFunctionDef(func, buf)
            fdef = function_pb2.FunctionDef()
            proto_data = c_api.TF_GetBuffer(buf)
            fdef.ParseFromString(compat.as_bytes(proto_data))
            with ops.init_scope():
                if context.executing_eagerly():
                    context.add_function(func)
                    self._function_deleter = _DefinedFunctionDeleter(
                        fdef.signature.name)
    exit(fdef)
exit(self._definition)
