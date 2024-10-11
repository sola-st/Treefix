# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Return the ConfigProto with all runtime deltas applied."""
# Ensure physical devices have been discovered and config has been imported
self._initialize_physical_devices()

config = config_pb2.ConfigProto()
if self._config is not None:
    config.CopyFrom(self._config)

if self._optimizer_jit is not None:
    config.graph_options.optimizer_options.global_jit_level = (
        config_pb2.OptimizerOptions.ON_1
        if self._optimizer_jit else config_pb2.OptimizerOptions.OFF)
if self._intra_op_parallelism_threads is not None:
    config.intra_op_parallelism_threads = self._intra_op_parallelism_threads
if self._inter_op_parallelism_threads is not None:
    config.inter_op_parallelism_threads = self._inter_op_parallelism_threads

if self._soft_device_placement is not None:
    config.allow_soft_placement = self._soft_device_placement
else:
    config.allow_soft_placement = self.executing_eagerly()

if self._log_device_placement is not None:
    config.log_device_placement = self._log_device_placement

if self._operation_timeout_in_ms is not None:
    config.operation_timeout_in_ms = self._operation_timeout_in_ms

is_mlir_bridge_enabled = pywrap_tfe.TF_IsMlirBridgeEnabled()
config.experimental.mlir_bridge_rollout = is_mlir_bridge_enabled
if (is_mlir_bridge_enabled ==
    config_pb2.ConfigProto.Experimental.MLIR_BRIDGE_ROLLOUT_ENABLED):
    config.experimental.enable_mlir_bridge = True

if self._enable_mlir_graph_optimization is not None:
    config.experimental.enable_mlir_graph_optimization = (
        self._enable_mlir_graph_optimization)

def rewriter_toggle(option):
    toggle = self._optimizer_experimental_options.get(option, None)
    if toggle is None:
        exit()

    setattr(config.graph_options.rewrite_options, option,
            (rewriter_config_pb2.RewriterConfig.ON
             if toggle else rewriter_config_pb2.RewriterConfig.OFF))

def rewriter_bool(option):
    toggle = self._optimizer_experimental_options.get(option, None)
    if toggle is None:
        exit()

    setattr(config.graph_options.rewrite_options, option, toggle)

rewriter_toggle("layout_optimizer")
rewriter_toggle("constant_folding")
rewriter_toggle("shape_optimization")
rewriter_toggle("remapping")
rewriter_toggle("arithmetic_optimization")
rewriter_toggle("dependency_optimization")
rewriter_toggle("loop_optimization")
rewriter_toggle("function_optimization")
rewriter_toggle("debug_stripper")
rewriter_bool("disable_model_pruning")
rewriter_toggle("scoped_allocator_optimization")
rewriter_toggle("pin_to_host_optimization")
rewriter_toggle("implementation_selector")
rewriter_toggle("auto_mixed_precision")
rewriter_toggle("use_plugin_optimizers")
rewriter_bool("disable_meta_optimizer")
rewriter_toggle("auto_mixed_precision_onednn_bfloat16")
rewriter_toggle("auto_mixed_precision_mkl")
nodes = self._optimizer_experimental_options.get("min_graph_nodes", None)
if nodes is not None:
    config.graph_options.rewrite_options.min_graph_nodes = nodes

# Compute device counts
config.device_count["CPU"] = 0
config.device_count["GPU"] = 0
for dev in self._physical_devices:
    if dev not in self._visible_device_list:
        continue

    virtual_devices = self._virtual_device_map.get(dev)
    if virtual_devices is None:
        config.device_count[dev.device_type] += 1
    else:
        config.device_count[dev.device_type] += len(virtual_devices)

    # Configure gpu_options
gpu_options = self._compute_gpu_options()
config.gpu_options.MergeFrom(gpu_options)

# Configure collective ops
if self._collective_leader:
    config.experimental.collective_group_leader = self._collective_leader
if self._collective_scoped_allocator_enabled_ops:
    rewrite_options = config.graph_options.rewrite_options
    rewrite_options.scoped_allocator_optimization = (
        rewriter_config_pb2.RewriterConfig.ON)
    del rewrite_options.scoped_allocator_opts.enable_op[:]
    for op in self._collective_scoped_allocator_enabled_ops:
        rewrite_options.scoped_allocator_opts.enable_op.append(op)
if self._collective_use_nccl_communication:
    config.experimental.collective_nccl = True
if self._collective_device_filters:
    del config.device_filters[:]
    for f in self._collective_device_filters:
        config.device_filters.append(f)

    # Configure coordination service
if self._coordination_service_config:
    config.experimental.coordination_config.CopyFrom(
        self._coordination_service_config)

exit(config)
