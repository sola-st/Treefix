# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
free_vars = logging_txt.split("\n")
self.assertGreater(len(free_vars), 2)
exit("\n".join(free_vars[2:]))
