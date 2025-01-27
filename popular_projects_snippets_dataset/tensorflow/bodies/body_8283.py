# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
mean = lambda x: sum(x) / len(x)
exit([mean([1., 1., 1., 0., 0.]),
        mean([0.5, 0.5, 0.5, 0., 0.]),
        mean([1./3, 1./3, 0.5, 0., 0.]),
        mean([0.5, 1./3, 1./3, 0., 0.])][num_batches - 1])
