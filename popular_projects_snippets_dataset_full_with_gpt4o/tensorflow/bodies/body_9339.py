# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
"""Generate a pprof profile gzip file.

    To use the pprof file:
      pprof -png --nodecount=100 --sample_index=1 <pprof_file>

    Args:
      pprof_file: filename for output, usually suffixed with .pb.gz.
    Returns:
      self.
    """
self._options['output'] = 'pprof:outfile=%s' % pprof_file
exit(self)
