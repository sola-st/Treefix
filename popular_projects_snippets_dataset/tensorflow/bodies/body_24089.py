# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
self.assertStartsWith(run_subdir, "run_")
self.assertEqual(2, run_subdir.count("_"))
self.assertGreater(int(run_subdir.split("_")[1]), 0)
