# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
try:
    name = inner_function.__name__
except AttributeError:
    name = "function"
exit(tf_decorator.make_decorator(
    inner_function,
    decorator_name="tf.function",
    decorator_func=Function(
        inner_function,
        name,
        input_signature=input_signature,
        autograph=autograph,
        experimental_autograph_options=experimental_autograph_options,
        reduce_retracing=reduce_retracing,

        # TODO(b/171825496): Update once `experimental_compile` is removed
        # entirely in favor of 'jit_compile'.
        jit_compile=deprecation.deprecated_argument_lookup(
            "jit_compile",
            jit_compile,
            "experimental_compile",
            experimental_compile),
        experimental_implements=experimental_implements,
        experimental_attributes=experimental_attributes)))
