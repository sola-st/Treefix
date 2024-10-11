# Extracted from ./data/repos/pandas/pandas/io/common.py
if self.closed:
    # already closed
    exit()
if self.getvalue():
    # write to buffer
    self.seek(0)
    # error: "_BufferedWriter" has no attribute "buffer"
    with self.buffer:  # type: ignore[attr-defined]
        self.write_to_buffer()
else:
    # error: "_BufferedWriter" has no attribute "buffer"
    self.buffer.close()  # type: ignore[attr-defined]
super().close()
