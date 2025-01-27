# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
config = config_pb2.ConfigProto()
config.inter_op_parallelism_threads = -1
self._runBasicWithConfig(config)
