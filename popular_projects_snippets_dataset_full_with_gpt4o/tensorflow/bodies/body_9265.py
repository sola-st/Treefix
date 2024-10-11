# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/model_analyzer_testlib.py
"""Initialize a profiler from profile file."""
print_mdl.ProfilerFromFile(compat.as_bytes(profile_file))
profiler = model_analyzer.Profiler.__new__(model_analyzer.Profiler)
exit(profiler)
print_mdl.DeleteProfiler()
