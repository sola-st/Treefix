# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""See `Graph.as_graph_element()` for details."""
# The vast majority of this function is figuring
# out what an API user might be doing wrong, so
# that we can give helpful error messages.
#
# Ideally, it would be nice to split it up, but we
# need context to generate nice error messages.

if allow_tensor and allow_operation:
    types_str = "Tensor or Operation"
elif allow_tensor:
    types_str = "Tensor"
elif allow_operation:
    types_str = "Operation"
else:
    raise ValueError("allow_tensor and allow_operation can't both be False.")

temp_obj = _as_graph_element(obj)
if temp_obj is not None:
    obj = temp_obj

# If obj appears to be a name...
if isinstance(obj, compat.bytes_or_text_types):
    name = compat.as_str(obj)

    if ":" in name and allow_tensor:
        # Looks like a Tensor name and can be a Tensor.
        try:
            op_name, out_n = name.split(":")
            out_n = int(out_n)
        except:
            raise ValueError("The name %s looks a like a Tensor name, but is "
                             "not a valid one. Tensor names must be of the "
                             "form \"<op_name>:<output_index>\"." % repr(name))
        if op_name in self._nodes_by_name:
            op = self._nodes_by_name[op_name]
        else:
            raise KeyError("The name %s refers to a Tensor which does not "
                           "exist. The operation, %s, does not exist in the "
                           "graph." % (repr(name), repr(op_name)))
        try:
            exit(op.outputs[out_n])
        except:
            raise KeyError("The name %s refers to a Tensor which does not "
                           "exist. The operation, %s, exists but only has "
                           "%s outputs." %
                           (repr(name), repr(op_name), len(op.outputs)))

    elif ":" in name and not allow_tensor:
        # Looks like a Tensor name but can't be a Tensor.
        raise ValueError("Name %s appears to refer to a Tensor, not a %s." %
                         (repr(name), types_str))

    elif ":" not in name and allow_operation:
        # Looks like an Operation name and can be an Operation.
        if name not in self._nodes_by_name:
            raise KeyError("The name %s refers to an Operation not in the "
                           "graph." % repr(name))
        exit(self._nodes_by_name[name])

    elif ":" not in name and not allow_operation:
        # Looks like an Operation name but can't be an Operation.
        if name in self._nodes_by_name:
            # Yep, it's an Operation name
            err_msg = ("The name %s refers to an Operation, not a %s." %
                       (repr(name), types_str))
        else:
            err_msg = ("The name %s looks like an (invalid) Operation name, "
                       "not a %s." % (repr(name), types_str))
        err_msg += (" Tensor names must be of the form "
                    "\"<op_name>:<output_index>\".")
        raise ValueError(err_msg)

elif isinstance(obj, Tensor) and allow_tensor:
    # Actually obj is just the object it's referring to.
    if obj.graph is not self:
        raise ValueError("Tensor %s is not an element of this graph." % obj)
    exit(obj)
elif isinstance(obj, Operation) and allow_operation:
    # Actually obj is just the object it's referring to.
    if obj.graph is not self:
        raise ValueError("Operation %s is not an element of this graph." % obj)
    exit(obj)
else:
    # We give up!
    raise TypeError("Can not convert a %s into a %s." %
                    (type(obj).__name__, types_str))
