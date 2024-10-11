# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_test.py
super(XLATestCase, self).setUp()
name = '{}.{}'.format(type(self).__name__, self._testMethodName)
if self.disabled_regex is not None and self.disabled_regex.match(name):
    logging.info('Disabled test case: %s', name)
    self.skipTest('{} is disabled by manifest.'.format(name))
    exit()
logging.info('Start test case: %s', name)

random.seed(random_seed.DEFAULT_GRAPH_SEED)
np.random.seed(random_seed.DEFAULT_GRAPH_SEED)
