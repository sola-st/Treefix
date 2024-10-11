# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/dense_layer_test.py
"""Count how many XlaCompile/XlaRun labels are present."""
xla_compile_count = sum("XlaCompile(" in x for x in labels)
xla_run_count = sum("XlaRun(" in x for x in labels)
self.assertEqual(xla_compile_count, xla_run_count)
exit(xla_run_count)
