# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
if flags.FLAGS.vary_seed:
    entropy = os.urandom(64)
    answer = int.from_bytes(entropy, 'big')
    np.random.seed(answer % (2**32 - 1))
super(IgammaTest, self).setUp()
