# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
"""Create a `ConcreteFunction` from `args`, `kwargs`, and `func_graph`."""
self.tracing_count += 1

arglen = len(args)
base_arg_names = self._function_spec.arg_names[:arglen]
num_missing_args = arglen - len(self._function_spec.arg_names)
missing_arg_names = [self._function_spec.vararg_name] * num_missing_args
# Produce a list of missing args of the form ["arg_0", "arg_1", ...],
# where arg is based on the self._function_spec.vararg_name.
missing_arg_names = [
    "%s_%d" % (arg, i) for i, arg in enumerate(missing_arg_names)
]
arg_names = base_arg_names + missing_arg_names
concrete_function = monomorphic_function.ConcreteFunction(
    func_graph_module.func_graph_from_py_func(
        self._name,
        self._python_function,
        args,
        kwargs,
        None,
        func_graph=func_graph,
        autograph=self._autograph,
        autograph_options=self._autograph_options,
        arg_names=arg_names,
        capture_by_value=self._capture_by_value,
        create_placeholders=False),
    self._function_attributes,
    spec=self.function_spec,
    # Tell the ConcreteFunction to clean up its graph once it goes out of
    # scope. This is not the default behavior since it gets used in some
    # places (like Keras) where the FuncGraph lives longer than the
    # ConcreteFunction.
    shared_func_graph=False)
exit(concrete_function)
