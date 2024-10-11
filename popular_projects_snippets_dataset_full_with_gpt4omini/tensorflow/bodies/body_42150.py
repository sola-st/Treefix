# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_graph_test.py
avg_time = (time.time() - start) / num_iters
dev = 'gpu' if tf.test.is_gpu_available() else 'cpu'
name = 'graph_%s_%s_batch_%d_%s' % (label, dev, batch_size, data_format())
extras = {'examples_per_sec': batch_size / avg_time}
self.report_benchmark(
    iters=num_iters, wall_time=avg_time, name=name, extras=extras)
