# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_ops_test.py
summ = summary_pb2.Summary()
summ.ParseFromString(s)
exit(summ)
