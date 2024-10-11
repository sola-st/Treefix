# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
exit(xla.variadic_sort(
    args,  # Pass the arguments as a tuple
    comparator=compare_lexicographic,
    dimension=0,
    is_stable=False))
