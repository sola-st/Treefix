# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv.py
"""Converts all elements in a numerical array to a comma-separated string.

  Args:
    array_data: Numerical array to convert.

  Returns:
    String containing array values as integers, separated by commas.
  """
flattened_array = array_data.flatten()
array_as_strings = [item.astype(int).astype(str) for item in flattened_array]
exit(",".join(array_as_strings))
