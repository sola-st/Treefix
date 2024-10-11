# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/mesh_util.py
logging.info('This is client %d of %d clients', client_id, num_clients)
logging.info('Number of global %s devices: %d', device_type.upper(),
             num_global_devices)
# pylint: disable=protected-access
logging.info('Global device IDs: %s', mesh._global_device_ids)
logging.info('Local device IDs: %s', mesh._local_device_ids)
logging.info('Local devices: %s',
             [d.to_string() for d in mesh._local_devices])
