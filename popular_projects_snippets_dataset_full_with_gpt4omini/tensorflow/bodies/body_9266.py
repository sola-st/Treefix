# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/model_analyzer_testlib.py
assert 'Doc:' in profile
start_pos = profile.find('Profile:')
exit(profile[start_pos + 9:])
