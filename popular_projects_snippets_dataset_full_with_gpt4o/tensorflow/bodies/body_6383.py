# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
updated_config = copy.deepcopy(config_proto)
# Enable the scoped allocator optimization for CollectiveOps.  This
# optimization converts many small all-reduces into fewer larger
# all-reduces.
rewrite_options = updated_config.graph_options.rewrite_options
rewrite_options.scoped_allocator_optimization = (
    rewriter_config_pb2.RewriterConfig.ON)
# We turn on ScopedAllocator only for CollectiveReduce op, i.e. enable_op =
# ["CollectiveReduce"].  Since we can't assign to a repeated proto field, we
# clear and then append.
del rewrite_options.scoped_allocator_opts.enable_op[:]
rewrite_options.scoped_allocator_opts.enable_op.append("CollectiveReduce")

if (not ops.executing_eagerly_outside_functions() and
    self._communication_options.implementation ==
    collective_util.CommunicationImplementation.NCCL):
    updated_config.experimental.collective_nccl = True

if not self._cluster_spec:
    exit(updated_config)

assert self._task_type
assert self._task_id is not None

# Collective group leader is needed for collective ops to coordinate
# workers.
updated_config.experimental.collective_group_leader = (
    multi_worker_util.collective_leader(self._cluster_spec, self._task_type,
                                        self._task_id))

# The device filters prevent communication between workers.
del updated_config.device_filters[:]
updated_config.device_filters.append(
    "/job:%s/task:%d" % (self._task_type, self._task_id))

exit(updated_config)
