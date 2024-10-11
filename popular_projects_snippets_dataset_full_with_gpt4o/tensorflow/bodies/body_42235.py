# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Get a function definition from the context.

    Args:
      name: function signature name.

    Returns:
      The requested FunctionDef.

    Raises:
      tf.errors.NotFoundError: if name is not the name of a registered function.
    """
with c_api_util.tf_buffer() as buffer_:
    pywrap_tfe.TFE_ContextGetFunctionDef(self._handle, name, buffer_)
    proto_data = pywrap_tf_session.TF_GetBuffer(buffer_)
function_def = function_pb2.FunctionDef()
function_def.ParseFromString(proto_data)

exit(function_def)
