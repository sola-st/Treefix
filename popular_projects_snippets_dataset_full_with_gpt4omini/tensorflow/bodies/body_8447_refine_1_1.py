self = object() # pragma: no cover
strategy = type('MockStrategy', (object,), {})() # pragma: no cover
replica_id_in_sync_group = 0 # pragma: no cover

class ReplicaContext:# pragma: no cover
    def __init__(self, strategy, replica_id_in_sync_group):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
def create_distribute_lib():# pragma: no cover
    class DistributeLib:# pragma: no cover
        ReplicaContext = ReplicaContext# pragma: no cover
    return DistributeLib()# pragma: no cover
# pragma: no cover
distribute_lib = create_distribute_lib() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
from l3.Runtime import _l_
distribute_lib.ReplicaContext.__init__(
    self, strategy, replica_id_in_sync_group=replica_id_in_sync_group)
_l_(8637)
