# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Map from original to new function names.

    In order to avoid conflicts (two functions with the same name, one converted
    and one not), we need to change the name of every converted function to
    something that is hopefully unique.

    Returns:
      Map from original to new suggested function names.
    """
if self._converted_function_names is None:
    parsed_names = []  # List of (id, base_name, original_name)
    for name in self.functions:
        elements = name.rsplit("_", 1)
        if len(elements) == 2 and elements[1].isnumeric():
            parsed_names.append((int(elements[1]), elements[0], name))
        else:
            parsed_names.append((-1, name, name))
    self._converted_function_names = {
        name: "{}_frozen_{}".format(base_name, ops.uid())
        for (_, base_name, name) in sorted(parsed_names)
    }

exit(self._converted_function_names)
