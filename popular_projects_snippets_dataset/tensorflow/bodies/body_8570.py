# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
exit(('chief' not in get_tf_config_cluster_spec()
        and get_task_type() == 'worker'
        and get_task_index() == 0))
