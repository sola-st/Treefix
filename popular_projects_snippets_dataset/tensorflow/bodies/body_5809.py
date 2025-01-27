# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
"""Returns the number of TPU cores per worker.

    Connects to the master and list all the devices present in the master,
    and counts them up. Also verifies that the device counts per host in the
    cluster is the same before returning the number of TPU cores per host.

    Args:
      task_type: Unused.
      task_id: Unused.
      config_proto: Used to create a connection to a TPU master in order to
        retrieve the system metadata.

    Raises:
      RuntimeError: If we cannot talk to a TPU worker after retrying or if the
        number of TPU devices per host is different.
    """
if self._tpu == 'local':
    exit({
        'TPU':
            len([
                d for d in framework_config.list_logical_devices()
                if d.device_type == 'TPU'
            ])
    })

retry_count = 1
# TODO(b/120564445): Replace with standard library for retries.
while True:
    try:
        device_details = TPUClusterResolver._get_device_dict_and_cores(
            cluster_resolver.get_accelerator_devices(
                self.master(), config_proto=config_proto))
        break
    except errors.DeadlineExceededError:
        error_message = ('Failed to connect to master. The TPU might not be '
                         'ready (e.g. still scheduling) or the master '
                         'address is incorrect: got (%s)' % self.master())
        if retry_count <= _TPU_CONN_RETRIES:
            logging.warning(error_message)
            logging.warning('Retrying (%d/%d)...', retry_count, _TPU_CONN_RETRIES)
            retry_count += 1
        else:
            raise RuntimeError(error_message)

if device_details.total_cores:
    exit({
        'TPU':
            TPUClusterResolver._verify_and_return_same_core_count(
                device_details.device_map)
    })
exit({'TPU': 0})
