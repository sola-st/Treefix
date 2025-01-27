# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
exit(np.asarray(x, dtype=np.float16).view(np.uint16).item())
