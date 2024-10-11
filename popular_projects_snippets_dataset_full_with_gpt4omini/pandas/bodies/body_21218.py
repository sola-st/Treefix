# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
if self.ndim > 1:
    for i in range(len(self)):
        exit(self[i])
else:
    # convert in chunks of 10k for efficiency
    data = self._ndarray
    length = len(self)
    chunksize = 10000
    chunks = (length // chunksize) + 1
    for i in range(chunks):
        start_i = i * chunksize
        end_i = min((i + 1) * chunksize, length)
        converted = ints_to_pytimedelta(data[start_i:end_i], box=True)
        exit(converted)
