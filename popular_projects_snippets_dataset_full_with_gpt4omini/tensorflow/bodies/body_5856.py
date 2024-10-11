# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver_test.py
worker1 = _create_pod_list(
    ('tensorflow-abc123', 'Running', '10.1.2.3'),
    ('tensorflow-def456', 'Running', '10.1.2.4'),
    ('tensorflow-999999', 'Running', '10.1.2.5'))
worker2 = _create_pod_list(
    ('tensorflow-abc124', 'Running', '10.1.2.6'),
    ('tensorflow-def457', 'Running', '10.1.2.7'),
    ('tensorflow-999990', 'Running', '10.1.2.8'))
ps = _create_pod_list(
    ('tensorflow-ps-1', 'Running', '10.1.2.1'),
    ('tensorflow-ps-2', 'Running', '10.1.2.2'))

cluster_resolver = KubernetesClusterResolver(
    job_to_label_mapping={
        'worker': ['job-name=worker1', 'job-name=worker2'],
        'ps': ['job-name=ps']
    },
    override_client=_mock_kubernetes_client({
        'job-name=worker1': worker1,
        'job-name=worker2': worker2,
        'job-name=ps': ps
    }))

actual_cluster_spec = cluster_resolver.cluster_spec()
expected_proto = """
    job {
      name: 'ps'
      tasks { key: 0 value: '10.1.2.1:8470' }
      tasks { key: 1 value: '10.1.2.2:8470' }
    }
    job {
      name: 'worker'
      tasks { key: 0 value: '10.1.2.5:8470' }
      tasks { key: 1 value: '10.1.2.3:8470' }
      tasks { key: 2 value: '10.1.2.4:8470' }
      tasks { key: 3 value: '10.1.2.8:8470' }
      tasks { key: 4 value: '10.1.2.6:8470' }
      tasks { key: 5 value: '10.1.2.7:8470' }
    }
    """
self._verifyClusterSpecEquality(actual_cluster_spec, str(expected_proto))
