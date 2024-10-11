# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
options = options_lib.Options()
options.autotune.enabled = True
options.autotune.cpu_budget = 10
options.autotune.ram_budget = 20
options.deterministic = True
options.experimental_external_state_policy = (
    options_lib.ExternalStatePolicy.FAIL)
options.experimental_distribute.auto_shard_policy = (
    options_lib.AutoShardPolicy.DATA)
options.experimental_distribute.num_devices = 1000
options.experimental_optimization.apply_default_optimizations = True
options.experimental_optimization.filter_fusion = True
options.experimental_optimization.filter_parallelization = True
options.experimental_optimization.inject_prefetch = False
options.experimental_optimization.map_and_batch_fusion = True
options.experimental_optimization.map_and_filter_fusion = True
options.experimental_optimization.map_fusion = True
options.experimental_optimization.map_parallelization = True
options.experimental_optimization.noop_elimination = True
options.experimental_optimization.parallel_batch = True
options.experimental_optimization.shuffle_and_repeat_fusion = True
options.experimental_slack = True
options.threading.max_intra_op_parallelism = 30
options.threading.private_threadpool_size = 40
pb = options._to_proto()
result = options_lib.Options()
result._from_proto(pb)
self.assertEqual(options, result)
