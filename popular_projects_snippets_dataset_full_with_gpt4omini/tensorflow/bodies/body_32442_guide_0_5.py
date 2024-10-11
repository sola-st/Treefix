from unittest.mock import Mock # pragma: no cover

ops = Mock() # pragma: no cover
check_ops = Mock(assert_near=Mock(side_effect=lambda x, y: None)) # pragma: no cover
array_ops = Mock(identity=Mock(side_effect=lambda x: x)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
larry = constant_op.constant([])
_l_(9580)
curly = constant_op.constant([])
_l_(9581)
with ops.control_dependencies([check_ops.assert_near(larry, curly)]):
    _l_(9583)

    out = array_ops.identity(larry)
    _l_(9582)
self.evaluate(out)
_l_(9584)
