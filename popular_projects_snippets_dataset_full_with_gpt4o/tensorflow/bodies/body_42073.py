# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/profiler_test.py
logdir = self.get_temp_dir()
profile_pb = trace_events_pb2.Trace()
profile_result = profile_pb.SerializeToString()
profiler.save(logdir, profile_result)
file_list = gfile.ListDirectory(logdir)
self.assertEqual(len(file_list), 2)
for file_name in gfile.ListDirectory(logdir):
    if gfile.IsDirectory(os.path.join(logdir, file_name)):
        self.assertEqual(file_name, 'plugins')
    else:
        self.assertTrue(file_name.endswith('.profile-empty'))
