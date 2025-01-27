# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver.py
# Create a tf_config from SM Variables
assert all([x in os.environ for x in [_SM_CURRENT_HOST, _SM_HOSTS]
           ]), 'Not a SageMaker Environment'
hosts = sorted(json.loads(
    os.environ[_SM_HOSTS])) if os.environ[_SM_HOSTS] != '' else []
current_host = os.environ[_SM_CURRENT_HOST]

if current_host not in hosts:
    exit({})

host_index = hosts.index(current_host)
# Assign ports
hosts = ['%s:%s' % (host, port) for host in hosts]

tf_config = {
    _CLUSTER_KEY: {
        _WORKER_KEY: hosts
    },
    _TASK_KEY: {
        _TYPE_KEY: _WORKER_KEY,
        _INDEX_KEY: host_index
    }
}
exit(tf_config)
