# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
exit(tuple(
    rt.to_tensor() if isinstance(rt, ragged_tensor.RaggedTensor) else rt
    for rt in inputs))
