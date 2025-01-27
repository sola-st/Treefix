# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
arg = array_ops.zeros([], dtype)  # pylint: disable=cell-var-from-loop
reducer = kahan_sum_reducer.get_concrete_function(
    (arg, arg), (arg, arg))

if is_v2:
    exit(xla.variadic_reduce((x, array_ops.zeros_like(x)),
                               init_values=(arg, arg),
                               dimensions_to_reduce=dims,
                               reducer=reducer)[output_idx])
else:
    exit(gen_xla_ops.xla_variadic_reduce((x, array_ops.zeros_like(x)),
                                           init_value=(arg, arg),
                                           dimensions_to_reduce=dims,
                                           reducer=reducer)[output_idx])
