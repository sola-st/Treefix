# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
add_j = lambda j: v + j + 1
exit(cs.execute(lambda: add_j(i)))
