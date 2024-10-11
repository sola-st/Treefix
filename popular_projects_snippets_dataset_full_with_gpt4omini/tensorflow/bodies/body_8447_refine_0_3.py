self = type('MockSelf', (object,), {})() # pragma: no cover
strategy = type('MockStrategy', (object,), {})() # pragma: no cover
replica_id_in_sync_group = 0 # pragma: no cover

class MockReplicaContext:# pragma: no cover
    def __init__(self, strategy, replica_id_in_sync_group):# pragma: no cover
        self.strategy = strategy# pragma: no cover
        self.replica_id_in_sync_group = replica_id_in_sync_group# pragma: no cover
strategy = type('MockStrategy', (object,), {})() # pragma: no cover
replica_id_in_sync_group = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
from l3.Runtime import _l_
distribute_lib.ReplicaContext.__init__(
    self, strategy, replica_id_in_sync_group=replica_id_in_sync_group)
_l_(8637)
