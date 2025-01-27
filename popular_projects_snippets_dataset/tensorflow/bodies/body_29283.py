# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/random_seed_test.py
tinput, toutput = input_fn(), output_fn()
self._checkEqual(tinput=tinput, toutput=toutput)
random_seed.set_random_seed(None)
