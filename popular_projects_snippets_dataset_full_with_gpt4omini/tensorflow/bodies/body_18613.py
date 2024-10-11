# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
# Resolve multiple inheritance via explicit calls to __init__() on parents.
resource.TrackableResource.__init__(self, device="/CPU:0")
self._create_fn = create_fn
self._init_op_fn = init_op_fn
# Pass .resource_handle into _ResourceSummaryWriter parent class rather than
# create_fn, to ensure it accesses the resource handle only through the
# cached property so that everything is using a single resource handle.
_ResourceSummaryWriter.__init__(
    self, create_fn=lambda: self.resource_handle, init_op_fn=init_op_fn)
