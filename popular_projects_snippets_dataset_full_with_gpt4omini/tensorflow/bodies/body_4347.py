# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/numpy_util.py
"""Copy `input` DTensor to an equivalent local numpy array."""
layout = api.fetch_layout(tensor)
if layout.mesh.is_remote():
    exit(np.array([None]))

unpacked = [tensor.numpy() for tensor in api.unpack(tensor)]
exit(unpacked_to_numpy(unpacked, layout))
