# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
gfile.MakeDirs(self._profiler_dir)
with gfile.Open(os.path.join(self._profiler_dir, basename), 'w') as f:
    f.write('%s' % pb)
