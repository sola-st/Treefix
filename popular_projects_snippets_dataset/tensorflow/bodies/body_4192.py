# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
"""A helper function to initialize multi-client tpu system."""

@def_function.function
def _tpu_init_fn():
    exit(gen_dtensor_ops.configure_and_initialize_global_tpu(
        use_tfrt_host_runtime=use_tfrt_host_runtime))

@def_function.function
def _set_global_tpu_array_fn(topology_proto):
    gen_dtensor_ops.d_tensor_set_global_tpu_array(topology_proto)

with ops.device("/job:" + config.full_job_name() + "/device:TPU_SYSTEM:0"):  # pylint: disable=protected-access
    my_core_ids = _tpu_init_fn()
logging.info("TPU core IDs: %s", my_core_ids)

# `my_core_ids` contains the IDs of TPU cores attached to this host.
#
# To generate correct and efficient XLA AllReduce group assignment, we must
# merge these arrays from all hosts and broadcast the result back to all
# hosts, so all hosts can use these mappings in their MLIR passes.
#
# This is essentially doing what WaitForDistributedTpuOp and
# SetGlobalTPUArrayOp do, in our multi-client environment.
num_devices_per_task = int(num_devices / num_tasks)

# Create a one-time use mesh and layout just for merging core IDs.
mesh = layout_lib.Mesh([_MESH_DIM_X],
                       *_create_device_array((num_devices,), _TPU_DEVICE_TYPE,
                                             config.client_id()))
layout = layout_lib.Layout([_MESH_DIM_X, layout_lib.UNSHARDED], mesh)
device = dtensor_device.DTensorDevice(meshes=[mesh])
logging.info("TPU core locations: %s",
             device.tpu_core_ids_to_locations(my_core_ids))

# At this point, we don't know which cores are attached to other hosts.
# The core ID mappings in the runtime haven't been set yet.
#
# The core ID merging AllReduce below is carefully written so it works
# without needing correct core mappings to be set in the runtime. We will
# use this AllReduce's result to set the core ID mappings, and all future
# user-initiated AllReduces will use the mappings.
#
# The runtime is hard-coded to ignore core ID mappings on this AllReduce.
all_core_ids = np.zeros([num_devices], dtype=np.int32)
for i in range(len(my_core_ids)):
    all_core_ids[task_id * num_devices_per_task + i] = my_core_ids[i]

# Only one local device gets valid input: 8 local core IDs among
# (num_tasks - 1) * 8 zeros. The 8 core IDs are set using task ID as offset.
# The other 7 local devices get zero inputs. All devices on all host
# participate in one AllReduce, whose result will be core IDs arranged by
# task-device ordinals.
all_core_ids = constant_op.constant([all_core_ids])
zeros = array_ops.zeros_like(all_core_ids)
all_core_ids = [all_core_ids] + [zeros] * (num_devices_per_task - 1)

with ops.device(device.name):
    all_core_ids = device.pack(all_core_ids, layout)
    all_core_ids = math_ops.reduce_sum(all_core_ids, axis=[0])
    unpacked_all_tpu_ids = device.unpack(all_core_ids)

all_core_ids = list(unpacked_all_tpu_ids[0].numpy())
logging.info("All TPU core IDs: %s", all_core_ids)

# Set the default core ID mappings in the runtime for legacy code and tests.
#
# Legacy code and tests create TPU meshes directly without using the
# `create_tpu_mesh` function below. Those meshes have global device IDs
# equal to TF task-device ordinals. The `all_core_ids` array happens to
# arrange core IDs by TF task-device ordinals. Using this array on those
# meshes guarantee correct although inefficient results.
device.set_tpu_core_ids("", all_core_ids)

# Remember enough global, immutable information to be able to build any ring
# we want prescribed by `create_tpu_mesh` in the future.
global _all_core_ids
_all_core_ids = all_core_ids

all_core_locations = device.tpu_core_ids_to_locations(all_core_ids)
all_core_locations = [
    _CoreLocation(l[0], l[1], l[2], l[3]) for l in all_core_locations
]
global _all_core_locations
_all_core_locations = all_core_locations
logging.info("All TPU core locations: %s", all_core_locations)

tpu_topology = _create_tpu_topology(all_core_locations, num_tasks,
                                    num_devices_per_task)

_set_global_tpu_array_fn(tpu_topology.serialized())
exit((tpu_topology, device))
