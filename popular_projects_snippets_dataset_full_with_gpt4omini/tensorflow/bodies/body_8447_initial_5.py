class MockBase(object): pass # pragma: no cover
distribute_lib = type('MockDistributeLib', (MockBase,), {'ReplicaContext': type('MockReplicaContext', (object,), {})})() # pragma: no cover
self = object() # pragma: no cover
replica_id_in_sync_group = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
from l3.Runtime import _l_
distribute_lib.ReplicaContext.__init__(
    self, strategy, replica_id_in_sync_group=replica_id_in_sync_group)
_l_(8637)
