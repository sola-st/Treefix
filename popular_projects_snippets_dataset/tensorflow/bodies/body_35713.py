# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
exit([cs.execute(lambda: fn(i)) for i in range(num_concurrent)])
