# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_tensor_op_test.py
summ = summary_pb2.Summary()
summ.ParseFromString(s)
self.assertEqual(len(summ.value), 1)
exit(summ.value[0])
