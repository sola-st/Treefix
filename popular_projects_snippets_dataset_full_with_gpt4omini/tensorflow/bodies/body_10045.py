# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/inspect_checkpoint.py
"""Prints tensors in a checkpoint file.

  If no `tensor_name` is provided, prints the tensor names and shapes
  in the checkpoint file.

  If `tensor_name` is provided, prints the content of the tensor.

  Args:
    file_name: Name of the checkpoint file.
    tensor_name: Name of the tensor in the checkpoint file to print.
    all_tensors: Boolean indicating whether to print all tensors.
    all_tensor_names: Boolean indicating whether to print all tensor names.
    count_exclude_pattern: Regex string, pattern to exclude tensors when count.
  """
try:
    reader = py_checkpoint_reader.NewCheckpointReader(file_name)
    if all_tensors or all_tensor_names:
        var_to_shape_map = reader.get_variable_to_shape_map()
        var_to_dtype_map = reader.get_variable_to_dtype_map()
        for key, value in sorted(var_to_shape_map.items()):
            print("tensor: %s (%s) %s" % (key, var_to_dtype_map[key].name, value))
            if all_tensors:
                try:
                    print(reader.get_tensor(key))
                except errors_impl.InternalError:
                    print("<not convertible to a numpy dtype>")
    elif not tensor_name:
        print(reader.debug_string().decode("utf-8", errors="ignore"))
    else:
        if not reader.has_tensor(tensor_name):
            print("Tensor %s not found in checkpoint" % tensor_name)
            exit()

        var_to_shape_map = reader.get_variable_to_shape_map()
        var_to_dtype_map = reader.get_variable_to_dtype_map()
        print("tensor: %s (%s) %s" %
              (tensor_name, var_to_dtype_map[tensor_name].name,
               var_to_shape_map[tensor_name]))
        print(reader.get_tensor(tensor_name))

    # Count total number of parameters
    print("# Total number of params: %d" % _count_total_params(
        reader, count_exclude_pattern=count_exclude_pattern))
except Exception as e:  # pylint: disable=broad-except
    print(str(e))
    if "corrupted compressed block contents" in str(e):
        print("It's likely that your checkpoint file has been compressed "
              "with SNAPPY.")
    if ("Data loss" in str(e) and
        any(e in file_name for e in [".index", ".meta", ".data"])):
        proposed_file = ".".join(file_name.split(".")[0:-1])
        v2_file_error_template = """
It's likely that this is a V2 checkpoint and you need to provide the filename
*prefix*.  Try removing the '.' and extension.  Try:
inspect checkpoint --file_name = {}"""
        print(v2_file_error_template.format(proposed_file))
