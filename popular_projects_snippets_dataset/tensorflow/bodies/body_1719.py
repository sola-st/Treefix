# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
exit(xla.variadic_sort(
    args,  # Pass the arguments as a tuple
    comparator=compare_lt,
    dimension=dimension,
    is_stable=False))
