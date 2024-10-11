# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/integration_test/profiler_api_test.py
path = os.path.join(logdir, 'plugins', 'profile', '*', '*.xplane.pb')
self.assertEqual(1, len(glob.glob(path)),
                 'Expected one path match: ' + path)
