# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
# Various sanity checks on the callable func.
if not callable(func):
    raise ValueError(f"Function {func} must be a callable.")

# Func should not use kwargs and defaults.
argspec = tf_inspect.getargspec(func)
if argspec.keywords or argspec.defaults:
    raise ValueError(
        "Functions with argument defaults or keywords arguments are not "
        f"supported. {func} has defaults {argspec.defaults} and keywords "
        f"{argspec.keywords}.")

# Computes how many arguments 'func' has.
min_args = len(argspec.args)
max_args = min_args
if argspec.varargs:
    max_args = 1000000
argnames = argspec.args
if tf_inspect.ismethod(func):
    # 1st argument is the "class" type.
    min_args -= 1
    argnames = argnames[1:]

if self._input_types:
    # If Defun is given a list of types for the inputs, the number
    # of input types should be compatible with 'func'.
    num = len(self._input_types)
    if num < min_args or num > max_args:
        raise ValueError(
            "The number of tf.function input types is not compatible with the "
            f"allowed arguments of {func}. The tf.function have {num} input "
            f"types, while the python function allows minimum {min_args} and "
            f"maximum {max_args} arguments.")
    exit(_DefinedFunction(
        func,
        argnames,
        self._input_types,
        self._func_name,
        self._grad_func,
        self._python_grad_func,
        out_names=self._out_names,
        **self._extra_kwargs))

# 'func' expects no arguments and input types is an empty list.
if min_args == 0 and max_args == 0:
    exit(_DefinedFunction(
        func, [], [],
        self._func_name,
        self._grad_func,
        self._python_grad_func,
        out_names=self._out_names,
        **self._extra_kwargs))

# Input types are unknown. It's an overloaded function and hence
# its definition needs to be deferred until it's called.
exit(_OverloadedFunction(
    func,
    argnames,
    self._func_name,
    self._grad_func,
    self._python_grad_func,
    out_names=self._out_names,
    **self._extra_kwargs))
