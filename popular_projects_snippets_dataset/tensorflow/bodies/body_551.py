# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/update/generate_v2_renames_map.py
"""Writes a Python dictionary mapping deprecated to canonical API names.

  Args:
    output_file_path: File path to write output to. Any existing contents
      would be replaced.
  """
function_renames = collect_function_renames()
constant_renames = collect_constant_renames()
all_renames = function_renames.union(constant_renames)
manual_renames = all_renames_v2.manual_symbol_renames

# List of rename lines to write to output file in the form:
#   'tf.deprecated_name': 'tf.canonical_name'
rename_lines = [
    get_rename_line(name, canonical_name)
    for name, canonical_name in all_renames
    if 'tf.' + name not in manual_renames
]
renames_file_text = '%srenames = {\n%s\n}\n' % (
    _FILE_HEADER, ',\n'.join(sorted(rename_lines)))
file_io.write_string_to_file(output_file_path, renames_file_text)
