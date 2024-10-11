# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
self.assertEqual(len(expected_specs), len(slices))
for i in range(len(expected_specs)):
    self.assertEqual(expected_specs[i], slices[i]._save_slice_info.spec)
