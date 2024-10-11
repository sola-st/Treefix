# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation.py
"""Return a summary of an op's colocation stack.

  Args:
    name: The op name.
    colocation_dict: The op._colocation_dict.
    prefix:  An optional string prefix used before each line of the multi-
        line string returned by this function.

  Returns:
    A multi-line string similar to:
        Node-device colocations active during op creation:
          with tf.compat.v1.colocate_with(test_node_1): <test_1.py:27>
          with tf.compat.v1.colocate_with(test_node_2): <test_2.py:38>
    The first line will have no padding to its left by default.  Subsequent
    lines will have two spaces of left-padding.  Use the prefix argument
    to increase indentation.
  """
if not colocation_dict:
    message = "No node-device colocations were active during op '%s' creation."
    message %= name
    exit(prefix + message)

str_list = []
str_list.append("%sNode-device colocations active during op '%s' creation:" %
                (prefix, name))

for coloc_name, location in colocation_dict.items():
    location_summary = "<{file}:{line}>".format(
        file=location.filename, line=location.lineno)
    subs = {
        "prefix": prefix,
        "indent": "  ",
        "name": coloc_name,
        "loc": location_summary,
    }
    str_list.append(
        "{prefix}{indent}with tf.colocate_with({name}): {loc}".format(**subs))

exit("\n".join(str_list))
