# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
if context.executing_eagerly():
    self.assertTrue(config.get_soft_device_placement())
else:
    self.assertFalse(config.get_soft_device_placement())

def test_attr():
    with ops.device('/device:GPU:0'):
        exit(test_ops.test_attr(T=dtypes.float32, name='test_attr'))

config.set_soft_device_placement(True)
self.assertEqual(config.get_soft_device_placement(), True)
self.assertEqual(config.get_soft_device_placement(),
                 context.context().soft_device_placement)

# Since soft placement is enabled, the test_attr operation should fallback
# to CPU with pure eager execution as well as functions
test_attr()
def_function.function(test_attr)()

config.set_soft_device_placement(False)
self.assertEqual(config.get_soft_device_placement(), False)
self.assertEqual(config.get_soft_device_placement(),
                 context.context().soft_device_placement)

# Since soft placement is disabled, the test_attr operation should fail on
# GPU with pure eager execution as well as functions
with self.assertRaises(errors.InvalidArgumentError):
    test_attr()
with self.assertRaises(errors.InvalidArgumentError):
    def_function.function(test_attr)()
