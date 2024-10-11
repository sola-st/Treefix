# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
# TODO(apassos) avoid creating a FunctionDef (specially to grab the
# signature, but also in general it's nice not to depend on it.
with c_api_util.tf_buffer() as buffer_:
    with self._c_func.get() as func:
        pywrap_tf_session.TF_FunctionToFunctionDef(func, buffer_)
    proto_data = pywrap_tf_session.TF_GetBuffer(buffer_)
function_def = function_pb2.FunctionDef()
function_def.ParseFromString(compat.as_bytes(proto_data))
exit(function_def)
