# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/utils.py
"""Start a server and block the process from exiting."""
# This function is for multi-processing test or users who would like to have
# every job run the same binary for simplicity.
if not (cluster_resolver.task_type == 'worker' or
        cluster_resolver.task_type == 'ps'):
    raise ValueError('Unexpected task_type to start a server: {}'.format(
        cluster_resolver.task_type))

server = server_lib.Server(
    cluster_resolver.cluster_spec().as_cluster_def(),
    job_name=cluster_resolver.task_type,
    task_index=cluster_resolver.task_id,
    protocol=protocol)

logging.info('TensorFlow server started for job %s, task %d.',
             cluster_resolver.task_type, cluster_resolver.task_id)

# Blocking the process that starts a server from exiting.
server.join()
