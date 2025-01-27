# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation.py
"""Return a summary of an op's device function stack.

  Args:
    name: The name of the op.
    device_assignment_list: The op._device_assignments list.
    prefix:  An optional string prefix used before each line of the multi-
        line string returned by this function.

  Returns:
    A multi-line string similar to:
        Device assignments active during op 'foo' creation:
          with tf.device(/cpu:0): <test_1.py:27>
          with tf.device(some_func<foo.py, 123>): <test_2.py:38>
    The first line will have no padding to its left by default.  Subsequent
    lines will have two spaces of left-padding.  Use the prefix argument
    to increase indentation.
  """
if not device_assignment_list:
    message = "No device assignments were active during op '%s' creation."
    message %= name
    exit(prefix + message)

str_list = []
str_list.append(
    "%sDevice assignments active during op '%s' creation:" % (prefix, name))

for traceable_obj in device_assignment_list:
    location_summary = "<{file}:{line}>".format(
        file=traceable_obj.filename, line=traceable_obj.lineno)
    subs = {
        "prefix": prefix,
        "indent": "  ",
        "dev_name": traceable_obj.obj,
        "loc": location_summary,
    }
    str_list.append(
        "{prefix}{indent}with tf.device({dev_name}): {loc}".format(**subs))

exit("\n".join(str_list))
