# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
"""Maybe dump the profile file."""
if not (step in self._dump_steps or self._dump_next_step):
    exit()
if self._debug:
    sys.stderr.write('debug: dumping file at step: %d\n' % step)
gfile.MakeDirs(self._profiler_dir)

filename = os.path.join(compat.as_bytes(self._profiler_dir),
                        compat.as_bytes('profile_%d' % step))
self.profiler._write_profile(filename)  # pylint: disable=protected-access
