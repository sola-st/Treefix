# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/random_seed_test.py
random_seed.set_random_seed(tinput[0])
g_seed, op_seed = data_random_seed.get_seed(tinput[1])
g_seed = self.evaluate(g_seed)
op_seed = self.evaluate(op_seed)
msg = "test_case = {0}, got {1}, want {2}".format(tinput, (g_seed, op_seed),
                                                  toutput)
self.assertEqual((g_seed, op_seed), toutput, msg=msg)
