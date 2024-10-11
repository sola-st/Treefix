# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    range_size = 5
    queue = inp.range_input_producer(
        range_size, shared_name="SHARED_NAME_XYZ", name="Q")
    self.assertProtoEquals("s: 'SHARED_NAME_XYZ'",
                           queue.queue_ref.op.node_def.attr["shared_name"])
