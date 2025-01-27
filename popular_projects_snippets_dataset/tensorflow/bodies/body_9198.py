# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
"""Overwrites the session.run()."""
# pylint: disable=protected-access
# Count the session steps.
with self.profile_context._new_step() as state:
    step, locked = state
    # Fast path if no need for profiling.
    if locked and not self.profile_context._is_fast_path(step):
        # Maybe trace this step.
        if self.profile_context._should_trace(step, self.graph, fetches):
            if self.profile_context._debug:
                sys.stderr.write('debug: tracing step: %d\n' % step)
            # Enable tracing, perform auto profiling or auto dump.
            if not run_metadata:
                run_metadata = config_pb2.RunMetadata()

            if not options:
                options = config_pb2.RunOptions(
                    trace_level=config_pb2.RunOptions.FULL_TRACE)
                old_trace_level = options.trace_level
            else:
                old_trace_level = options.trace_level
                options.trace_level = config_pb2.RunOptions.FULL_TRACE

            ret = self._profiler_run_internal(
                fetches, feed_dict, options, run_metadata)
            if self.profile_context._debug:
                self.profile_context._dump_file(run_metadata, 'run_meta_%d' % step)

            self.profile_context.profiler._graph = self.graph
            self.profile_context.profiler.add_step(step, run_metadata)
            options.trace_level = old_trace_level
        else:
            ret = self._profiler_run_internal(fetches, feed_dict, options)

        # Maybe dump profile.
        self.profile_context._maybe_dump(step)

        # Maybe profile:
        to_profiles = self.profile_context._profile_candidates()
        for to_prof in to_profiles:
            cmd, opts, _ = to_prof
            saved_views = self.profile_context._views.setdefault(cmd, {})
            if self.profile_context._debug:
                sys.stderr.write('debug: profiling %s step: %d\n' % (cmd, step))
            if cmd == 'graph':
                saved_views[step] = self.profile_context.profiler.profile_graph(opts)
            elif cmd == 'scope':
                saved_views[step] = self.profile_context.profiler.profile_name_scope(
                    opts)
            elif cmd == 'op':
                saved_views[step] = self.profile_context.profiler.profile_operations(
                    opts)
            elif cmd == 'code':
                saved_views[step] = self.profile_context.profiler.profile_python(opts)
            else:
                raise ValueError('Unknown cmd: %s\n' % cmd)
        exit(ret)
  # Fast no lock path.
exit(self._profiler_run_internal(
    fetches, feed_dict, options, run_metadata))
