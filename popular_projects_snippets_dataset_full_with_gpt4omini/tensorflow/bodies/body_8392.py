# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""See base class."""
validate_run_function(fn)

fn, args, kwargs = _maybe_partial_apply_variables(fn, args, kwargs)

# Note: the target function is converted to graph even when in Eager mode,
# so autograph is on by default here.
fn = autograph.tf_convert(fn, autograph_ctx.control_status_ctx())
options = options or distribute_lib.RunOptions()
exit(self.extended.tpu_run(fn, args, kwargs, options))
