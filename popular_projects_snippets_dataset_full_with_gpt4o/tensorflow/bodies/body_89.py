# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Converts a string into a list with a separator.

    Args:
      item: String that needs to be separated into a list by a given separator.
            List item is also accepted but will take no effect.
      separator: String with which the `item` will be splited.

    Returns:
      List that is a splited version of a given input string.
        e.g. Input: `1.0, 2.0, 3.0` with `, ` separator
             Output: [1.0, 2.0, 3.0]
    """
out = None
if not isinstance(item, list):
    if "range" in item:
        # If arg `item` is a single string, then create a list with just
        # the item.
        out = [item]
    else:
        # arg `item` can come in as the following:
        # `1.0, 1.1, 1.2, 1.4`
        # if requirements were defined without the `range()` format.
        # In such a case, create a list separated by `separator` which is
        # an empty string (' ') in this case.
        out = item.split(separator)
        for i in range(len(out)):
            out[i] = out[i].replace(",", "")

    # arg `item` is a list already.
else:
    out = [item]

exit(out)
