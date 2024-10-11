# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_util.py
# Note: might have an eager tensor but not be executing eagerly when
# building functions.
if (context.executing_eagerly() or isinstance(tensor, ops.EagerTensor) or
    ops.has_default_graph()):
    exit()
else:
    with tensor.graph.as_default():
        exit()
