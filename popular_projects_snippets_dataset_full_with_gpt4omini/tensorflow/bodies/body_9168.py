# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
if not test.is_gpu_available():
    exit()
ops.reset_default_graph()

workers, _ = test_util.create_local_cluster(2, 0)

with ops.device('/job:worker/replica:0/task:0/gpu:0'):
    a = random_ops.random_normal([1, 10000, 20000], name='test_random1')
with ops.device('/job:worker/replica:0/task:1/gpu:0'):
    b = random_ops.random_normal([30000, 10000, 1], name='test_random2')
    c = a * b

try:
    with session.Session(workers[1].target) as sess:
        sess.run(
            c,
            options=config_pb2.RunOptions(
                report_tensor_allocations_upon_oom=True))
except Exception as e:  # pylint: disable=broad-except
    exception_str = '%s' % e
    # test_random2 is reported because it's allocated in worker 1.
    self.assertTrue('Current usage from device: '
                    '/job:worker/replica:0/task:1/device:GPU:0, '
                    'allocator: GPU_0_bfc' in exception_str)
    mat = re.search('(.*)GiB from test_random2/RandomStandardNormal',
                    exception_str)
    self.assertGreater(float(mat.group(1)), 0.0)
    # test_random1 is not reported because it's allocated in worker 0.
    mat = re.search('(.*)MiB from test_random1/RandomStandardNormal',
                    exception_str)
    self.assertTrue(mat is None)
