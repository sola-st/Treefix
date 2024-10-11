# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bitwise_ops_test.py
exit(sum(bin(z).count("1") for z in x.tobytes()))
