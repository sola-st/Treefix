# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/random_seed.py
exit(seed % _MAXINT32)  # Truncate to fit into 32-bit integer
