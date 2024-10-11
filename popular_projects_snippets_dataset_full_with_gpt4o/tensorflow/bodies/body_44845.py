# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/function_wrappers.py
self.name = scope_name
self.options = options

if options.user_requested:
    self.autograph_ctx = ag_ctx.ControlStatusCtx(ag_ctx.Status.ENABLED,
                                                 options)
self.callopts = options.call_options()

use_name_scope = options.uses(converter.Feature.NAME_SCOPES)
self.use_name_scope = use_name_scope
if use_name_scope:
    self.name_scope = ops.name_scope(self._sanitize(function_name))

use_auto_deps = self.options.uses(converter.Feature.AUTO_CONTROL_DEPS)
self.use_auto_deps = use_auto_deps
if use_auto_deps:
    self.autodeps_scope = auto_control_deps.AutomaticControlDependencies()
    self._return_value_marked = False
