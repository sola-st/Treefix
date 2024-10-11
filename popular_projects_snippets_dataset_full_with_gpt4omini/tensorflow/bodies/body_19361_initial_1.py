from collections import deque # pragma: no cover

class MockAPI(object): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.queue = deque([1, 2, 3]) # pragma: no cover
 # pragma: no cover
    def dequeue(self): # pragma: no cover
        return self.queue.popleft() if self.queue else None # pragma: no cover
 # pragma: no cover
mid_level_api = MockAPI() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
from l3.Runtime import _l_
aux = mid_level_api.dequeue()
_l_(10101)
exit(aux)
