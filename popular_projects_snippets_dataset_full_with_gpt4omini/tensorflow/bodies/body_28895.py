# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/get_single_element_test.py
_ = dataset1_fn().get_single_element()
_ = dataset2_fn().get_single_element()
exit("hello")
