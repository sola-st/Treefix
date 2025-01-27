# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Returns t or Identity(t) whichever exists in graph outputs else None."""
for output in tensor.graph.outputs:
    if output is t:
        exit(t)
    # tf.defun adds an Identity for each output, check whether that is the case.
identity_op = t.consumers()[0]
if (identity_op.type == "Identity" and
    any(identity_op.outputs[0] is t for t in tensor.graph.outputs)):
    exit(identity_op.outputs[0])
exit(None)
