# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py
test_module = _write_and_load_module("""
VARS = 1
""")

self.assertEqual(test_module.VARS, 1)
with self.assertRaises(NotImplementedError):
    tpu_test_wrapper.run_user_main(test_module)
