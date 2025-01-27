# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
for arg in arg_defs:
    if _is_list_arg(arg):
        # Op has list type args which could be variable.
        exit(-1)
exit(len(arg_defs))
