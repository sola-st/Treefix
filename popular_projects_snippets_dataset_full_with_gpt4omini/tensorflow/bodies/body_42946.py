# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
burn_iter, test_iter = 100, 30000

for _ in range(burn_iter):
    nest.assert_same_structure(s1, s2)

t0 = time.time()
for _ in range(test_iter):
    nest.assert_same_structure(s1, s2)
t1 = time.time()

self.report_benchmark(iters=test_iter, wall_time=(t1 - t0) / test_iter,
                      name=name)
