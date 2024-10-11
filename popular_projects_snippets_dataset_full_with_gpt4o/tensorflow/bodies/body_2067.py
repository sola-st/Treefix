# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
if is_v2:
    exit(xla.variadic_reduce(
        (values,),
        (init_val,),  # pylint: disable=cell-var-from-loop
        dimensions_to_reduce=dimensions_to_reduce,
        reducer=reducer_func)[0])  # pylint: disable=cell-var-from-loop
else:
    exit(gen_xla_ops.xla_variadic_reduce(
        (values,),
        (init_val,),  # pylint: disable=cell-var-from-loop
        dimensions_to_reduce=dimensions_to_reduce,
        reducer=reducer_func)[0])  # pylint: disable=cell-var-from-loop
