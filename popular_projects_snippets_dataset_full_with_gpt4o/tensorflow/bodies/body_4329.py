# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/mesh_util.py
"""Runs a barrier on the mesh.

  Upon returning from the barrier, all operations run before the barrier
  would have completed across all clients. Currently we allocate a fully
  sharded tensor with mesh shape and run an all_reduce on it.

  Example:

  A barrier can be used before application exit to ensure completion of pending
  ops.

  ```python

  x = [1, 2, 3]
  x = dtensor.relayout(x, dtensor.Layout.batch_sharded(mesh, 'batch', 1))
  dtensor.barrier(mesh)

  # At this point all devices on all clients in the mesh have completed
  # operations before the barrier. Therefore it is OK to tear down the clients.
  sys.exit()
  ```

  Args:
    mesh: The mesh to run the barrier on.
    barrier_name: The name of the barrier. Mainly used for logging purpose.
    timeout_in_ms: The timeout of the barrier in ms. If omitted, blocks
      indefinitely till the barrier is reached from all clients.
  """
if barrier_name is None:
    barrier_name = '(barrier)'

logging.info('entering barrier before op: %s', barrier_name)

# Make sure all ops are consumed before running the sync.
context.async_wait()

# Reduction on a fully sharded tensor requires all devices to participate
# and serves as a barrier on the mesh.
component = array_ops.reshape(1.0, [1] * len(mesh.shape()))
ones = api.pack([component] * mesh.num_local_devices(),
                layout.Layout(mesh.dim_names, mesh))

mesh_size = math_ops.reduce_sum(ones)
if mesh_size != mesh.size:
    raise ValueError(
        'Global barrier produced wrong mesh size : {0} while mesh has actual'
        'size : {1}'.format(mesh_size, mesh.size))

# TODO(hthu): This isn't strictly needed but might cause confusing behaviors
# from users. Consider dropping this if there is a `big` performance hit.
context.async_wait()

if context.context().coordination_service:
    if timeout_in_ms is None:
        timeout_in_ms = 24 * 60 * 60 * 1000  # 24 hours to stand in for infinite.

    num_calls = _BARRIER_DICT.setdefault(barrier_name, 0)
    _BARRIER_DICT[barrier_name] = num_calls + 1

    barrier_id = f'{barrier_name}:{num_calls}'
    context.context().wait_at_barrier(barrier_id, timeout_in_ms)

logging.info('finished running barrier across all clients after '
             'op: %s', barrier_name)
