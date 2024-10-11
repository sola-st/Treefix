# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
exit((np.concatenate([[p] * int(w) for p, w in zip(predictions, weights)]),
        np.concatenate([[l] * int(w) for l, w in zip(labels, weights)])))
