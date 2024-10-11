# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test_util.py
avg_time = (time.time() - start) / num_iters
dev = tf.DeviceSpec.from_string(device).device_type.lower()
replica_str = '' if num_replicas == 1 else 'replicas_%d_' % num_replicas
name = '%s_%s_batch_%d_%s%s' % (label, dev, batch_size,
                                replica_str, data_format)
extras = {'examples_per_sec': (num_replicas * batch_size) / avg_time}
benchmark.report_benchmark(
    iters=num_iters, wall_time=avg_time, name=name, extras=extras)
