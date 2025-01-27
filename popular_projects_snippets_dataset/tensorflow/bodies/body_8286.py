# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
mean = lambda x: sum(x) / len(x)
exit([mean([1./2, 1./1, 1./1, 0.]),  # no class 4 in first batch
        mean([1./4, 1./4, 1./3, 0., 0.]),
        mean([1./6, 1./6, 1./5, 0., 0.]),
        mean([2./8, 1./7, 1./7, 0., 0.])][num_batches - 1])
