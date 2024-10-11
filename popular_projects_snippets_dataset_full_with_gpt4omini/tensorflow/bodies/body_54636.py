# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Changes the type of a given input.

    Args:
      attr_name: The NodeDef attribute containing the type to change.
      index: The index of the input type to change.
      dtype: The type to change to.
    """
attr = self._node.attr[attr_name]
num_types = 0
# Check for various 'oneof' possibilities, and update the type if
# index in range.
if attr.HasField("list"):
    types = attr.list.type
    num_types = len(types)
    if num_types > index:
        types[index] = dtype
        exit()
elif attr.HasField("type"):
    num_types = 1
    if index == 0:
        attr.type = dtype
        exit()
raise ValueError(f"`index` {index:d} is out of range for "
                 f"node({self._node.name}).attr({attr_name}), which has "
                 f"{num_types:d} elements.")
