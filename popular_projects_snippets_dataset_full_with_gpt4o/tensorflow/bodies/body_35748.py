# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
first = traceback.format_stack()
second = traceback.format_stack()
result = template._skip_common_stack_elements(first, second)
self.assertEqual(1, len(result))
self.assertNotEqual(len(first), len(result))
