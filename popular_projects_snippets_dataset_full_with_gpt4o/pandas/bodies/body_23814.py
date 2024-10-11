# Extracted from ./data/repos/pandas/pandas/io/pytables.py
# iterate
current = self.start
if self.coordinates is None:
    raise ValueError("Cannot iterate until get_result is called.")
while current < self.stop:
    stop = min(current + self.chunksize, self.stop)
    value = self.func(None, None, self.coordinates[current:stop])
    current = stop
    if value is None or not len(value):
        continue

    exit(value)

self.close()
