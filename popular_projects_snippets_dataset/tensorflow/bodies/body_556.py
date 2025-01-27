# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/update/generate_v2_reorders_map.py
"""Writes a Python dictionary mapping function name to argument order.

  Args:
    output_file_path: File path to write output to. Any existing contents
      would be replaced.
  """
reordered_function_names = (
    tf_upgrade_v2.TFAPIChangeSpec().reordered_function_names)

all_reorders = collect_function_arg_names(reordered_function_names)

# List of reorder lines to write to output file in the form:
#   'tf.function_name': ['arg1', 'arg2', ...]
rename_lines = [
    get_reorder_line(name, arg_names)
    for name, arg_names in all_reorders.items()]
renames_file_text = '%sreorders = {\n%s\n}\n' % (
    _FILE_HEADER, ',\n'.join(sorted(rename_lines)))
file_io.write_string_to_file(output_file_path, renames_file_text)
