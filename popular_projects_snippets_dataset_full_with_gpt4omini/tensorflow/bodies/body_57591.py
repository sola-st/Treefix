# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert.py
if values is None:
    # Handling `--boolean_flag`.
    # Without additional arguments, it implies true.
    flag_value = True
elif values.lower() == "true":
    # Handling `--boolean_flag=true`.
    # (Case insensitive after the equal sign)
    flag_value = True
elif values.lower() == "false":
    # Handling `--boolean_flag=false`.
    # (Case insensitive after the equal sign)
    flag_value = False
else:
    raise ValueError("Invalid argument to --{}. Must use flag alone,"
                     " or specify true/false.".format(self.dest))
setattr(namespace, self.dest, flag_value)
