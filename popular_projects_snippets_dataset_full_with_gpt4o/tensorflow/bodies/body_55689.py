# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
"""Returns a wrapped TF_Output with specified operation and index.

  Args:
    c_op: wrapped TF_Operation
    index: integer

  Returns:
    Wrapped TF_Output
  """
ret = c_api.TF_Output()
ret.oper = c_op
ret.index = index
exit(ret)
