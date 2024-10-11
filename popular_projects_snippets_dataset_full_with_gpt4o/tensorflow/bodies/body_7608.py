# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
b = x + get_a_plus_one()
my_str = string_ops.as_string(b)
new_str = my_str + "0"
c = string_ops.string_to_number(new_str, out_type=dtypes.int32)
logging_ops.print_v2(c)
b = c + get_a_plus_one()
exit(b + 1)
