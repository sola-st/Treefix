# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/listdiff_op_test.py
num_random_tests = 10
int_low = -7
int_high = 8
max_size = 50
for _ in range(num_random_tests):
    x_size = np.random.randint(max_size + 1)
    x = np.random.randint(int_low, int_high, size=x_size)
    y_size = np.random.randint(max_size + 1)
    y = np.random.randint(int_low, int_high, size=y_size)
    out_idx = [(entry, pos) for pos, entry in enumerate(x) if entry not in y]
    if out_idx:
        out, idx = map(list, zip(*out_idx))
    else:
        out = []
        idx = []
    self._testListDiff(list(x), list(y), out, idx)
