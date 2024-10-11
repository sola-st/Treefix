# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/kernels_test.py
kernel_list = kernels.get_all_registered_kernels()
self.assertGreater(len(kernel_list.kernel), 0)
