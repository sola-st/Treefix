# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
# In both branches below, the template store is installed as default after
# the variable scope is opened in order to ensure that templates nested at
# the same level correctly uniquify lower variable scope names.
if self._variable_scope:
    # Create a cache for the variable scope context manager the first time
    # around so that we don't have to keep recreating it.
    if not self._variable_scope_context_manager:
        self._variable_scope_context_manager = variable_scope.variable_scope(
            self._variable_scope, reuse=variable_scope.AUTO_REUSE)
    with self._variable_scope_context_manager:
        with self._template_store.as_default():
            exit(self._call_func(args, kwargs))
else:
    # The scope was not created at construction time, so create it here.
    # Subsequent calls should reuse variables.
    with variable_scope.variable_scope(
        self._unique_name, self._name,
        custom_getter=self._custom_getter) as vs:
        self._variable_scope = vs
        # Because the scope was not created at construction time, the template
        # store's variable scope name is unset; set it here.
        self._template_store.set_variable_scope_name(vs.name)
        with self._template_store.as_default():
            exit(self._call_func(args, kwargs))
