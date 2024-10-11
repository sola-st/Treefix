# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
config = config_pb2.ConfigProto()
config.experimental.executor_type = "SINGLE_THREADED_EXECUTOR"
self._runBasicWithConfig(config)
