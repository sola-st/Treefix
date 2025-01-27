# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
exit(lambda state, _: (_sparse(state.values[0] + step), state))
