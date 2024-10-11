# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
time_dir = os.path.join(test.get_temp_dir(), 'time')
memory_dir = os.path.join(test.get_temp_dir(), 'memory')
profile_dir = os.path.join(test.get_temp_dir(), 'dir/dir2/profile')
# TODO(xpan): Should we create parent directory for them?
gfile.MkDir(time_dir)
gfile.MkDir(memory_dir)

time_opts = (
    builder(builder.time_and_memory()).with_file_output(
        os.path.join(time_dir, 'profile')).select(['micros']).build())
memory_opts = (
    builder(builder.time_and_memory()).with_file_output(
        os.path.join(memory_dir, 'profile')).select(['bytes']).build())

time_steps = [2, 3]
memory_steps = [1, 3]
dump_steps = [3, 4]

x = lib.BuildSmallModel()
with profile_context.ProfileContext(
    profile_dir, trace_steps=[1, 2, 3], dump_steps=[3, 4]) as pctx:
    pctx.add_auto_profiling('scope', time_opts, time_steps)
    pctx.add_auto_profiling('scope', memory_opts, memory_steps)

    self._trainLoop(x, 10, time_dir, time_steps, memory_dir, memory_steps,
                    profile_dir, dump_steps)
