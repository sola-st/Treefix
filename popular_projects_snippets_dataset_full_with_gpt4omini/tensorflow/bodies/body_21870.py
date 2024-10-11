# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    source_strings = ["A", "B", "D", "G"]
    source_ints = [7, 3, 5, 2]
    slices = inp.slice_input_producer(
        [source_strings, source_ints],
        shared_name="SHARED_NAME_XYZ",
        name="sip")

    self.assertProtoEquals(
        "s: 'SHARED_NAME_XYZ'",
        slices[0].op.inputs[1].op.inputs[0].op.node_def.attr["shared_name"])
