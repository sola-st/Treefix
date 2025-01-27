# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
options = xla_client.CompileOptions()
executable_build_options = options.executable_build_options
options.num_replicas = 3
options.num_partitions = 2
options.profile_version = 1337
options.compile_portable_executable = True
executable_build_options.num_replicas = 3
executable_build_options.num_partitions = 2
executable_build_options.debug_options.xla_cpu_enable_fast_math = True
executable_build_options.debug_options.xla_test_all_input_layouts = True

b = options.SerializeAsString()
restored = xla_client.CompileOptions.ParseFromString(b)

for name in ("num_replicas", "num_partitions", "profile_version",
             "compile_portable_executable"):
    self.assertEqual(getattr(options, name), getattr(restored, name),
                     msg=name)

for name in ("num_replicas", "num_partitions"):
    self.assertEqual(getattr(options.executable_build_options, name),
                     getattr(restored.executable_build_options, name),
                     msg=name)

for name in ("xla_cpu_enable_fast_math", "xla_test_all_input_layouts"):
    self.assertEqual(
        getattr(options.executable_build_options.debug_options, name),
        getattr(restored.executable_build_options.debug_options, name),
        msg=name)
