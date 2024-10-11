# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/config_test.py
self.assertEqual(config.client_id(), 0)
self.assertEqual(config.num_clients(), 1)
self.assertEqual(config.job_name(), 'localhost')
self.assertEqual(config.full_job_name(), 'localhost/replica:0/task:0')
self.assertEqual(config.jobs(), [])
