# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/config_test.py
# bns names must be sorted in the bns order.
dtensor_jobs = [
    '/bns/localhost/{task_id}'.format(task_id=i) for i in range(16)
]
os.environ[config._DT_JOBS] = ','.join(dtensor_jobs)
self.assertListEqual(dtensor_jobs, config.jobs())

dtensor_jobs = [
    '/bns/localhost/{task_id}:8888'.format(task_id=i) for i in range(16)
]
os.environ[config._DT_JOBS] = ','.join(dtensor_jobs)
self.assertListEqual(dtensor_jobs, config.jobs())

dtensor_jobs = [
    '/bns/localhost/{task_id}'.format(task_id=100 - i) for i in range(16)
]
os.environ[config._DT_JOBS] = ','.join(dtensor_jobs)
with self.assertRaisesRegex(ValueError, 'Unexpected DTENSOR_JOBS'):
    config.jobs()
