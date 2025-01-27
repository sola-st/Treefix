# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
exit(xla.variadic_sort([x],
                         dimension=0,
                         is_stable=False,
                         comparator=compare_gt))
