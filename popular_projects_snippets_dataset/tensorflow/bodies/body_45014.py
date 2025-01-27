# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class FaultyBinding:

    def __array__(self):
        raise ValueError('fault')

bad_obj = FaultyBinding()

def fail_if_warning(*_):
    self.fail('No warning should be issued')

with test.mock.patch.object(ag_logging, 'warning', fail_if_warning):
    with self.assertRaisesRegex(ValueError, 'fault'):
        api.converted_call(
            np.power, (bad_obj, 2), None, options=DEFAULT_RECURSIVE)
