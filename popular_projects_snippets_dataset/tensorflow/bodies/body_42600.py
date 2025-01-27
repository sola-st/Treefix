# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cloud_tpu_test.py
# Log full diff on failure.
self.maxDiff = None  # pylint:disable=invalid-name

self.assertCountEqual(
    EXPECTED_DEVICES_PRE_CONNECT,
    [device.name for device in config.list_logical_devices()])

resolver = tpu_cluster_resolver.TPUClusterResolver(
    tpu=FLAGS.tpu, zone=FLAGS.zone, project=FLAGS.project
)
remote.connect_to_cluster(resolver)

expected_devices = EXPECTED_DEVICES_PRE_CONNECT
for task in range(FLAGS.num_tpu_devices // DEVICES_PER_TASK):
    expected_devices.extend([
        template.format(task=task)
        for template in EXPECTED_NEW_DEVICES_AFTER_CONNECT_TEMPLATES
    ])

self.assertCountEqual(
    expected_devices,
    [device.name for device in config.list_logical_devices()])

tpu_strategy_util.initialize_tpu_system(resolver)
