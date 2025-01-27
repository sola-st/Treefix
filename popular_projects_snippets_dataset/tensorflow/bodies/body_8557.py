# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
with self._coord.stop_on_exception():
    os.environ['TF_CONFIG'] = json.dumps(tf_config)
    # Force the new thread simulating a worker to run in the same context
    # mode as the parent thread does.
    if executing_eagerly:
        with context.eager_mode():
            task_fn(*args, **kwargs)
    else:
        with ops.Graph().as_default(), context.graph_mode():
            task_fn(*args, **kwargs)
