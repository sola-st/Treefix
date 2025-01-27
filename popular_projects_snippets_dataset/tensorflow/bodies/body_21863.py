# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    strings = [b"to", b"be", b"or", b"not", b"to", b"be"]
    queue = inp.string_input_producer(
        strings, shared_name="SHARED_NAME_XYZ", name="Q")
    self.assertProtoEquals("s: 'SHARED_NAME_XYZ'",
                           queue.queue_ref.op.node_def.attr["shared_name"])
