# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
exit(xla.variadic_reduce(
    values,
    (
        init_val_1,  # pylint: disable=cell-var-from-loop
        init_val_2,  # pylint: disable=cell-var-from-loop
    ),
    dimensions_to_reduce=dimensions_to_reduce,
    reducer=reducer_func))  # pylint: disable=cell-var-from-loop
