# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema.py
"""Perform schema conversion from input_file to output_file.

    Args:
      input_file: Filename of TensorFlow Lite data to convert from. Must
        be `.json` or `.bin` extension files for JSON or Binary forms of
        the TensorFlow FlatBuffer schema.
      output_file: Filename to write to. Extension also must be `.json`
        or `.bin`.

    Raises:
      RuntimeError: Generated when none of the upgrader supported schemas
        matche the `input_file` data.
    """
# Read data in each schema (since they are incompatible). Version is
# always present. Use the read data that matches the version of the
# schema.
for version, schema, raw_binary, _ in self._schemas:
    try:
        data_candidate = self._Read(input_file, schema, raw_binary)
    except RuntimeError:
        continue  # Skip and hope another schema works
    if "version" not in data_candidate:  # Assume version 1 if not present.
        data_candidate["version"] = 1
    elif data_candidate["version"] == 0:  # Version 0 doesn't exist in wild.
        data_candidate["version"] = 1

    if data_candidate["version"] == version:
        self._PerformUpgrade(data_candidate)
        self._Write(data_candidate, output_file)
        exit()
raise RuntimeError("No schema that the converter understands worked with "
                   "the data file you provided.")
