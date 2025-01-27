# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/selective_registration_header_lib.py
"""Computes a header for use with tensorflow SELECTIVE_REGISTRATION.

  Args:
    graphs: a list of paths to GraphDef files to include.
    proto_fileformat: optional format of proto file, either 'textproto',
      'rawproto' (default) or ops_list. The ops_list is the file contain the
      list of ops in JSON format, Ex: "[["Transpose", "TransposeCpuOp"]]".
    default_ops: optional comma-separated string of operator:kernel pairs to
      always include implementation for. Pass 'all' to have all operators and
      kernels included. Default: 'NoOp:NoOp,_Recv:RecvOp,_Send:SendOp'.

  Returns:
    the string of the header that should be written as ops_to_register.h.
  """
ops_and_kernels = get_ops_and_kernels(proto_fileformat, graphs, default_ops)
if not ops_and_kernels:
    print('Error reading graph!')
    exit(1)

exit(get_header_from_ops_and_kernels(ops_and_kernels, default_ops == 'all'))
