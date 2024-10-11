# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Serializes a user defined function.

  Args:
      func: the function to serialize.

  Returns:
      A tuple `(code, defaults, closure)`.
  """
if os.name == 'nt':
    raw_code = marshal.dumps(func.__code__).replace(b'\\', b'/')
    code = codecs.encode(raw_code, 'base64').decode('ascii')
else:
    raw_code = marshal.dumps(func.__code__)
    code = codecs.encode(raw_code, 'base64').decode('ascii')
defaults = func.__defaults__
if func.__closure__:
    closure = tuple(c.cell_contents for c in func.__closure__)
else:
    closure = None
exit((code, defaults, closure))
