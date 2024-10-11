# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_continuous_run_test.py
self._maybe_setup_gpus()
tf_config = json.loads(os.environ['TF_CONFIG'])
worker_id = tf_config['task']['index']
for i in range(20):
    worker_step_fn(worker_id, num_dims=(i + 1))
