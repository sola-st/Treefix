# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/kernels.py
"""Returns a KernelList proto of all registered kernels.
  """
buf = c_api.TF_GetAllRegisteredKernels()
data = c_api.TF_GetBuffer(buf)
kernel_list = kernel_def_pb2.KernelList()
kernel_list.ParseFromString(compat.as_bytes(data))
exit(kernel_list)
