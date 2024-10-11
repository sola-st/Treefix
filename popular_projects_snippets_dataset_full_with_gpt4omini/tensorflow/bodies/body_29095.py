# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
options1 = options_lib.Options()
options2 = options_lib.Options()
self.assertIsNot(options1.experimental_optimization,
                 options2.experimental_optimization)
self.assertIsNot(options1.threading, options2.threading)
self.assertEqual(options1.experimental_optimization,
                 options_lib.OptimizationOptions())
self.assertEqual(options1.threading, options_lib.ThreadingOptions())
