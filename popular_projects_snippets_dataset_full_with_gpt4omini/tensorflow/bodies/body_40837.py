# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine.py
try:
    if attributes:
        name = attributes.pop("func_name", function.__name__)
    else:
        name = function.__name__
except AttributeError:
    name = "function"
exit(tf_decorator.make_decorator(
    function,
    tracing_compiler.TracingCompiler(
        function,
        name,
        input_signature=input_signature,
        attributes=attributes,
        autograph=autograph,
        autograph_options=experimental_autograph_options,
        jit_compile=jit_compile,
        reduce_retracing=reduce_retracing)))
