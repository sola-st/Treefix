# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver_test.py
name_to_ip = {}
instance_list = []
for instance in instances:
    name_to_ip[instance['name']] = instance['ip']
    instance_list.append({
        'instance': 'https://gce.example.com/gce/res/' + instance['name']
    })

mock_instance = self.standard_mock_instances(name_to_ip)
mock_instance_group = self.standard_mock_instance_groups(instance_list)

exit(self.standard_mock_service_client(mock_instance_group, mock_instance))
