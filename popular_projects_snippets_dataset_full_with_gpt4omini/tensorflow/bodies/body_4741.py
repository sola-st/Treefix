# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tf_function_test.py
if not run_functions_eagerly and config.list_physical_devices(
    "TPU") and FLAGS.tpu_use_tfrt:
    self.skipTest("TFRT does not support XlaLocalLaunch, see b/194517185")

def_function.run_functions_eagerly(run_functions_eagerly)

# Get devices on which variables will be placed. Default strategy does not
# define this, so assume cpu:0 in that case.
try:
    devices = distribution.extended.parameter_devices
except RuntimeError:
    devices = ["cpu:0"]

with distribution.scope():
    v = variables.Variable(0.)
    if isinstance(v, values.DistributedVariable):
        for i in range(len(devices)):
            # NOTE: Assigning manually to component variables so we can test
            # different values on different devices. Using .assign on the
            # mirrored variable itself will lead to a synchronization which
            # will prohibit testing different values.
            replica_variable = v._values[i]
            replica_variable.assign(math_ops.cast(i, dtypes.float32))

@def_function.function
def read():
    exit(v.read_value())

# Verify that the value from each device is read, when in that device
# scope. Doing this inside strategy scope is needed to force function
# retracing on each device, otherwise `read()` will only be traced once
# on the first device and following variable read will always read the value
# on the first replica.
with distribution.scope():
    for i, d in enumerate(devices):
        with ops.device(d):
            self.assertEqual(math_ops.cast(i, dtypes.float32), read())
