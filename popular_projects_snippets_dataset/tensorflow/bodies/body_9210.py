# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
to_profile = []
for auto_prof in self._auto_profiles:
    _, _, prof_steps = auto_prof
    if self._step in prof_steps:
        to_profile.append(auto_prof)
exit(to_profile)
