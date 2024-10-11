# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_v2_test.py
logdir = self.get_temp_dir()
profiler.start(logdir)
with trace.Trace('three_times_five'):
    three = constant_op.constant(3)
    five = constant_op.constant(5)
    product = three * five
self.assertAllEqual(15, product)

profiler.stop()
file_list = gfile.ListDirectory(logdir)
self.assertEqual(len(file_list), 1)
for file_name in gfile.ListDirectory(logdir):
    if gfile.IsDirectory(os.path.join(logdir, file_name)):
        self.assertEqual(file_name, 'plugins')
profile_dir = os.path.join(logdir, 'plugins', 'profile')
run = gfile.ListDirectory(profile_dir)[0]
hostname = socket.gethostname()
xplane = os.path.join(profile_dir, run, hostname + '.xplane.pb')
self.assertTrue(gfile.Exists(xplane))
