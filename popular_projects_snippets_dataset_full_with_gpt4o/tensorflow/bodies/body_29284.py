# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/random_seed_test.py
random_seed.set_random_seed(1)
for i in range(10):
    tinput = (1, None)
    toutput = (1, i)
    self._checkEqual(tinput=tinput, toutput=toutput)
