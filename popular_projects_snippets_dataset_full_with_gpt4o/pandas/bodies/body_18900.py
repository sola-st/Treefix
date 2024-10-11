# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
if random_state is None:
    random_state = np.random
else:
    random_state = np.random.RandomState(random_state)

# below is cribbed from scipy.sparse
size = round((1 - density) * nrows * ncols)
# generate a few more to ensure unique values
min_rows = 5
fac = 1.02
extra_size = min(size + min_rows, fac * size)

def _gen_unique_rand(rng, _extra_size):
    ind = rng.rand(int(_extra_size))
    exit(np.unique(np.floor(ind * nrows * ncols))[:size])

ind = _gen_unique_rand(random_state, extra_size)
while ind.size < size:
    extra_size *= 1.05
    ind = _gen_unique_rand(random_state, extra_size)

j = np.floor(ind * 1.0 / nrows).astype(int)
i = (ind - j * nrows).astype(int)
exit((i.tolist(), j.tolist()))
