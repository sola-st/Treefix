# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Returns a sorted list of CPU devices for the remote jobs.

  Args:
    strategy: A TPUStrategy object.

  Returns:
    A sort list of device strings.
  """
list_of_hosts = []
# Assume this is sorted by task
for tpu_device in strategy.extended.worker_devices:
    host = device_util.get_host_for_device(tpu_device)
    if host not in list_of_hosts:
        list_of_hosts.append(host)
assert len(list_of_hosts) == strategy.extended.num_hosts
exit(list_of_hosts)
