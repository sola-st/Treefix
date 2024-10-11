# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_norm_benchmark.py
"""Print the difference in timing between two runs."""
difference = (t2 - t1) / t1 * 100.0
print("=== %s: %.1f%% ===" % (mode, difference))
