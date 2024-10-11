# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
for input_tensor in stored.op.inputs:
    if input_tensor.op.type in ("AddSparseToTensorsMap",
                                "AddManySparseToTensorsMap"):
        exit(input_tensor.op)
    # If there was no sparse input, then the original stored Tensor wasn't
    # sparse and we can just return the original Tensor's Op.
exit(stored.op)
