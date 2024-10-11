# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_system_metadata.py
"""Automatically detects the TPU system metadata in the system."""
tpu_core_count = 0
devices = []
device_dict = collections.defaultdict(list)

if context.executing_eagerly():
    logical_devices = config.list_logical_devices()

    # We want the output type to match in both eager and session mode
    devices = [session_lib._DeviceAttributes(device_util.canonicalize(d.name),  # pylint: disable=protected-access
                                             d.device_type, 0, 0)
               for d in logical_devices]
else:
    # TODO(b/120564445): Replace with standard library for retries.
    retry_count = 1
    while True:
        logging.info('Querying Tensorflow master (%s) for TPU system metadata.',
                     master_address)
        try:
            with ops.Graph().as_default():
                with session_lib.Session(
                    master_address,
                    config=get_session_config_with_timeout(
                        _PINGING_MASTER_TIMEOUT_IN_MS,
                        cluster_def)) as sess:
                    devices = sess.list_devices()
                    break
        except errors.DeadlineExceededError:
            msg = ('Failed to connect to the Tensorflow master. The TPU worker may '
                   'not be ready (still scheduling) or the Tensorflow master '
                   'address is incorrect: got (%s).' %
                   (master_address))

            # TODO(xiejw): For local or grpc master we might not need retry logic
            # here.
            if retry_count <= _RETRY_TIMES:
                logging.warning('%s', msg)
                logging.warning('Retrying (%d/%d).', retry_count, _RETRY_TIMES)
                retry_count += 1
            else:
                raise ValueError(msg)

for device in devices:
    spec = tf_device.DeviceSpec.from_string(device.name)
    if spec.device_type == 'TPU':
        device_dict[spec.task].append(spec.device_index)
        tpu_core_count += 1

num_of_cores_per_host = 0
if tpu_core_count:
    num_cores_per_host_set = set(
        [len(core_ids) for core_ids in device_dict.values()])
    if len(num_cores_per_host_set) != 1:
        raise RuntimeError(
            'TPU cores on each host is not same. This should not happen!. '
            'devices: {}'.format(devices))
    num_of_cores_per_host = num_cores_per_host_set.pop()

topology = None
if query_topology:
    if not tpu_core_count:
        raise RuntimeError(
            'Cannot find any TPU cores in the system (master address {}). '
            'This usually means the master address is incorrect or the '
            'TPU worker has some problems. Available devices: {}'.format(
                master_address, devices))

    topology = _obtain_topology(master_address, cluster_def)

# We sort the metadata devices so that downstream users get a sorted list
# for creating mirrored variables correctly.
def _sort_key(device):
    spec = tf_device.DeviceSpec.from_string(device.name)
    exit((spec.job, spec.replica, spec.task, spec.device_type,
            spec.device_index))
devices = tuple(sorted(devices, key=_sort_key))

metadata = TPUSystemMetadata(
    num_cores=tpu_core_count,
    num_hosts=len(device_dict),
    num_of_cores_per_host=num_of_cores_per_host,
    topology=topology,
    devices=devices)

if tpu_core_count:
    logging.info('Found TPU system:')
    logging.info('*** Num TPU Cores: %d', metadata.num_cores)
    logging.info('*** Num TPU Workers: %d', metadata.num_hosts)
    logging.info('*** Num TPU Cores Per Worker: %d',
                 metadata.num_of_cores_per_host)
    for device in metadata.devices:
        logging.info('*** Available Device: %s', device)
else:
    logging.info('Failed to find TPU: %s', metadata)
exit(metadata)
