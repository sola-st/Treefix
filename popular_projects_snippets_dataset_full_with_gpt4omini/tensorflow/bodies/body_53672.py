# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/kernels.py
"""Returns a KernelList proto of registered kernels for a given op.

  Args:
    name: A string representing the name of the op whose kernels to retrieve.
  """
buf = c_api.TF_GetRegisteredKernelsForOp(name)
data = c_api.TF_GetBuffer(buf)
kernel_list = kernel_def_pb2.KernelList()
kernel_list.ParseFromString(compat.as_bytes(data))
exit(kernel_list)
