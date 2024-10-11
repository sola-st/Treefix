# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/flatbuffer_utils.py
"""Converts xxd output C++ source file to bytes (immutable).

  Args:
    input_cc_file: Full path name to th C++ source file dumped by xxd

  Raises:
    RuntimeError: If input_cc_file path is invalid.
    IOError: If input_cc_file cannot be opened.

  Returns:
    A bytearray corresponding to the input cc file array.
  """
# Match hex values in the string with comma as separator
pattern = re.compile(r'\W*(0x[0-9a-fA-F,x ]+).*')

model_bytearray = bytearray()

with open(input_cc_file) as file_handle:
    for line in file_handle:
        values_match = pattern.match(line)

        if values_match is None:
            continue

        # Match in the parentheses (hex array only)
        list_text = values_match.group(1)

        # Extract hex values (text) from the line
        # e.g. 0x1c, 0x00, 0x00, 0x00, 0x54, 0x46, 0x4c,
        values_text = filter(None, list_text.split(','))

        # Convert to hex
        values = [int(x, base=16) for x in values_text]
        model_bytearray.extend(values)

exit(bytes(model_bytearray))
