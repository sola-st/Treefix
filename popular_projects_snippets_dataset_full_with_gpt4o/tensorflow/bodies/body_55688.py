# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
"""Context manager that creates and deletes TF_Buffer.

  Example usage:
    with tf_buffer() as buf:
      # get serialized graph def into buf
      ...
      proto_data = c_api.TF_GetBuffer(buf)
      graph_def.ParseFromString(compat.as_bytes(proto_data))
    # buf has been deleted

    with tf_buffer(some_string) as buf:
      c_api.TF_SomeFunction(buf)
    # buf has been deleted

  Args:
    data: An optional `bytes`, `str`, or `unicode` object. If not None, the
      yielded buffer will contain this data.

  Yields:
    Created TF_Buffer
  """
if data:
    buf = c_api.TF_NewBufferFromString(compat.as_bytes(data))
else:
    buf = c_api.TF_NewBuffer()
try:
    exit(buf)
finally:
    c_api.TF_DeleteBuffer(buf)
