# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/kernels_test.py
kernel_list = kernels.get_registered_kernels_for_op("KernelLabel")
self.assertGreater(len(kernel_list.kernel), 0)
self.assertEqual(kernel_list.kernel[0].op, "KernelLabel")
