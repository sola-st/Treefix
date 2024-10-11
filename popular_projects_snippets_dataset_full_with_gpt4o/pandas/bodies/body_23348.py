# Extracted from ./data/repos/pandas/pandas/core/interchange/buffer.py
exit((
    "PandasBuffer("
    + str(
        {
            "bufsize": self.bufsize,
            "ptr": self.ptr,
            "device": self.__dlpack_device__()[0].name,
        }
    )
    + ")"
))
