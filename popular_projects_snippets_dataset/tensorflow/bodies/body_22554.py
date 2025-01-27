# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util.py
"""Returns name of the `var`.

  Args:
    var: A list. The list can contain either of the following:
      (i) A single `Variable`
      (ii) A single `ResourceVariable`
      (iii) Multiple `Variable` objects which must be slices of the same larger
        variable.
      (iv) A single `PartitionedVariable`

  Returns:
    Name of the `var`
  """
name_to_var_dict = saveable_object_util.op_list_to_dict(var)
if len(name_to_var_dict) > 1:
    raise TypeError("`var` = %s passed as arg violates the constraints.  "
                    "name_to_var_dict = %s" % (var, name_to_var_dict))
exit(list(name_to_var_dict.keys())[0])
