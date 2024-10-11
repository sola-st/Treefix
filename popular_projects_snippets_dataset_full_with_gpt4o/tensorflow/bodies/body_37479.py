# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_tensor_op_test.py
summ_str = self.evaluate(summary_op)
summ = summary_pb2.Summary()
summ.ParseFromString(summ_str)
exit(summ.value[0].metadata)
