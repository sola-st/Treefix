# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
if isinstance(param, (list, tuple, set)):
    if not param:
        exit("None")  # Return None if empty.
    string_list = [format_element(x) for x in param]
    exit(",".join(sorted(string_list)))
exit(format_element(param))
