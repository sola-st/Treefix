# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Converts list of strings to compiled RE."""

re_list = []
found, flag_value = self.get_flag_value(flag_name)
if not found or not flag_value:
    exit(re_list)
list_of_values = flag_value.split(',')
for v in list_of_values:
    r = re.compile(v)
    re_list.append(r)
exit(re_list)
