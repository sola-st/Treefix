# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/config_test.py
# The ip port format is not a bns address, and not required to sorted.
dtensor_jobs = ['localhost:{port}'.format(port=16 - i) for i in range(16)]
os.environ[config._DT_JOBS] = ','.join(dtensor_jobs)
self.assertListEqual(dtensor_jobs, config.jobs())
