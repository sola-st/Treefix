# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
if not test.is_gpu_available():
    exit()
ops.reset_default_graph()
with ops.device('/device:GPU:0'):
    a = random_ops.random_normal([1, 10000, 20000], name='test_random1')
    b = random_ops.random_normal([30000, 10000, 1], name='test_random2')
    c = a * b

try:
    with session.Session(config=self._no_rewrite_session_config()) as sess:
        sess.run(
            c,
            options=config_pb2.RunOptions(
                report_tensor_allocations_upon_oom=True))
except Exception as e:  # pylint: disable=broad-except
    exception_str = '%s' % e
    # This trace reports allocations for to random tensor.
    self.assertTrue('OOM when allocating tensor with shape[30000,10000,20000]'
                    in exception_str)
    mat = re.search('(.*)GiB from test_random2/RandomStandardNormal',
                    exception_str)
    self.assertGreater(float(mat.group(1)), 0.0)
    mat = re.search('(.*)MiB from test_random1/RandomStandardNormal',
                    exception_str)
    self.assertGreater(float(mat.group(1)), 0.0)
