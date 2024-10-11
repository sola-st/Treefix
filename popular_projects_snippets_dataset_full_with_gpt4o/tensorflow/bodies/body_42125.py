# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
device, data_format = resnet50_test_util.device_and_data_format()
model = resnet50.ResNet50(data_format)
tf.compat.v2.summary.experimental.set_step(
    tf.compat.v1.train.get_or_create_global_step())
logdir = tempfile.mkdtemp()
with tf.compat.v2.summary.create_file_writer(
    logdir, max_queue=0,
    name='t0').as_default(), tf.compat.v2.summary.record_if(True):
    with tf.device(device), context.execution_mode(execution_mode):
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.1)
        images, labels = resnet50_test_util.random_batch(2, data_format)
        apply_gradients(model, optimizer,
                        compute_gradients(model, images, labels))
        self.assertEqual(320, len(model.variables))
        context.async_wait()
events = events_from_logdir(logdir)
self.assertEqual(len(events), 2)
self.assertEqual(events[1].summary.value[0].tag, 'loss')
