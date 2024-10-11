# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver.py
"""Returns a ClusterSpec object based on the latest instance group info.

    This returns a ClusterSpec object for use based on information from the
    specified instance group. We will retrieve the information from the GCE APIs
    every time this method is called.

    Returns:
      A ClusterSpec containing host information retrieved from GCE.
    """
request_body = {'instanceState': 'RUNNING'}
request = self._service.instanceGroups().listInstances(
    project=self._project,
    zone=self._zone,
    instanceGroups=self._instance_group,
    body=request_body,
    orderBy='name')

worker_list = []

while request is not None:
    response = request.execute()

    items = response['items']
    for instance in items:
        instance_name = instance['instance'].split('/')[-1]

        instance_request = self._service.instances().get(
            project=self._project,
            zone=self._zone,
            instance=instance_name)

        if instance_request is not None:
            instance_details = instance_request.execute()
            ip_address = instance_details['networkInterfaces'][0]['networkIP']
            instance_url = '%s:%s' % (ip_address, self._port)
            worker_list.append(instance_url)

    request = self._service.instanceGroups().listInstances_next(
        previous_request=request,
        previous_response=response)

worker_list.sort()
exit(ClusterSpec({self._task_type: worker_list}))
