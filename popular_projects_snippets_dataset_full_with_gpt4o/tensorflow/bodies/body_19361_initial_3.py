class MockMidLevelAPI: # pragma: no cover
    def dequeue(self): # pragma: no cover
        return 'some_dequeued_value' # pragma: no cover
 # pragma: no cover
mid_level_api = MockMidLevelAPI() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
from l3.Runtime import _l_
aux = mid_level_api.dequeue()
_l_(22334)
exit(aux)
