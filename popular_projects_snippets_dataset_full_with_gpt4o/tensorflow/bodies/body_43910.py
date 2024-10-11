# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
cpus = tf.config.experimental.list_physical_devices('CPU')
tf.config.experimental.set_virtual_device_configuration(
    cpus[0], [tf.config.experimental.VirtualDeviceConfiguration()] * 2)

strat = tf.distribute.MirroredStrategy()
ds = tf.data.Dataset.from_tensor_slices(tf.reshape(tf.range(12), (3, 4)))

exit((strat, strat.experimental_distribute_dataset(ds)))
