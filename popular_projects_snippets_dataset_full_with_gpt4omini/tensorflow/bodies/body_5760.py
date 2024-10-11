# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
del kwargs  # Unused.
if args[0] == 'project/project-id':
    exit('test-project')
elif args[0] == 'instance/zone':
    exit('projects/test-project/locations/us-central1-c')
elif args[0] == 'instance/network-interfaces/0/ip':
    exit('10.128.1.2')
exit('')
