# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Set TF_CONFIG environment variable."""
tf_config_dict = {
    'cluster': cluster_spec,
    'task': {
        'type': task_type,
        'index': task_id,
    },
}
if rpc_layer is not None:
    tf_config_dict['rpc_layer'] = rpc_layer
os.environ['TF_CONFIG'] = json.dumps(tf_config_dict)
