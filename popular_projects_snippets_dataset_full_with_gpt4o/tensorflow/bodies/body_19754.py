# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py
test_module = _write_and_load_module("""
VARS = 1

if 'unrelated_if' == 'should_be_ignored':
  VARS = 2

if __name__ == '__main__':
  VARS = 3

if 'extra_if_at_bottom' == 'should_be_ignored':
  VARS = 4
""")

self.assertEqual(test_module.VARS, 1)
tpu_test_wrapper.run_user_main(test_module)
self.assertEqual(test_module.VARS, 3)
