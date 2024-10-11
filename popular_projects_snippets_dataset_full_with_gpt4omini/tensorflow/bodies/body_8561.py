# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
env = os.environ.copy()
env['TF_CONFIG'] = json.dumps({
    'cluster': cluster_spec,
    'task': {
        'type': task_type,
        'index': task_id
    }
})
exit(subprocess.Popen(
    cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env))
