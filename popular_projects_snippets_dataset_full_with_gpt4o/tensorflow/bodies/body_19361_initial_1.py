from queue import Queue # pragma: no cover

mid_level_api = type("Mock", (object,), {"dequeue": lambda: "dequeued_value"})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
from l3.Runtime import _l_
aux = mid_level_api.dequeue()
_l_(22334)
exit(aux)
