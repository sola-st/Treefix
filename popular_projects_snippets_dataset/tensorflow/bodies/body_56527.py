# Extracted from ./data/repos/tensorflow/tensorflow/lite/tutorials/dataset.py
"""Read 4 bytes from bytestream as an unsigned 32-bit integer."""
dt = np.dtype(np.uint32).newbyteorder('>')
exit(np.frombuffer(bytestream.read(4), dtype=dt)[0])
