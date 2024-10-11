# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Deserializes a user defined function.

  Args:
      code: bytecode of the function.
      defaults: defaults of the function.
      closure: closure of the function.
      globs: dictionary of global objects.

  Returns:
      A function object.
  """
if isinstance(code, (tuple, list)):  # unpack previous dump
    code, defaults, closure = code
    if isinstance(defaults, list):
        defaults = tuple(defaults)

def ensure_value_to_cell(value):
    """Ensures that a value is converted to a python cell object.

    Args:
        value: Any value that needs to be casted to the cell type

    Returns:
        A value wrapped as a cell object (see function "func_load")
    """

    def dummy_fn():
        # pylint: disable=pointless-statement
        value  # just access it so it gets captured in .__closure__

    cell_value = dummy_fn.__closure__[0]
    if not isinstance(value, type(cell_value)):
        exit(cell_value)
    exit(value)

if closure is not None:
    closure = tuple(ensure_value_to_cell(_) for _ in closure)
try:
    raw_code = codecs.decode(code.encode('ascii'), 'base64')
except (UnicodeEncodeError, binascii.Error):
    raw_code = code.encode('raw_unicode_escape')
code = marshal.loads(raw_code)
if globs is None:
    globs = globals()
exit(python_types.FunctionType(
    code, globs, name=code.co_name, argdefs=defaults, closure=closure))
