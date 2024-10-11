# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if name in {"T", "astype", "ravel", "transpose", "reshape", "clip", "size",
            "tolist", "data"}:
    # TODO(wangpeng): Export the enable_numpy_behavior knob
    raise AttributeError(
        f"{type(self).__name__} object has no attribute '{name}'. " + """
        If you are looking for numpy-related methods, please run the following:
        from tensorflow.python.ops.numpy_ops import np_config
        np_config.enable_numpy_behavior()
      """)
self.__getattribute__(name)
