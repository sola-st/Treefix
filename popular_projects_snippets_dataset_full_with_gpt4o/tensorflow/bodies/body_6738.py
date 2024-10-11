# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
self._result = 0
self._lock = threading.Lock()
self._init_condition = threading.Condition()
self._init_reached = 0
self._finish_condition = threading.Condition()
self._finish_reached = 0
self._sess_config = config_pb2.ConfigProto(allow_soft_placement=True)
super(ParameterServerStrategyTestBase, self).setUp()
