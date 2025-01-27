# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Transforms a function. See GenericTranspiler.trasnform_function.

    This overload wraps the parent's `transform_function`, adding caching and
    facilities to instantiate the output as a Python object. It also
    adds facilities to make new symbols available to the generated Python code,
    visible as local variables - see `get_extra_locals`.

    Args:
      fn: A function or lambda.
      user_context: An opaque object (may be None) that is forwarded to
        transform_ast, through the ctx.user attribute.
    Returns:
      A tuple:
        * A function or lambda with the same signature and closure as `fn`
        * The temporary module into which the transformed function was loaded
        * The source map as a
            Dict[origin_info.LineLocation, origin_info.OriginInfo]
    """
cache_subkey = self.get_caching_key(user_context)

if self._cache.has(fn, cache_subkey):
    # Fast path: use a lock-free check.
    factory = self._cached_factory(fn, cache_subkey)

else:
    with self._cache_lock:
        # Check again under lock.
        if self._cache.has(fn, cache_subkey):
            factory = self._cached_factory(fn, cache_subkey)

        else:
            logging.log(1, '%s is not cached for subkey %s', fn, cache_subkey)
            # TODO(mdan): Confusing overloading pattern. Fix.
            nodes, ctx = super(PyToPy, self).transform_function(fn, user_context)

            if isinstance(nodes, gast.Lambda):
                nodes = gast.Assign(
                    targets=[
                        gast.Name(
                            ctx.info.name,
                            ctx=gast.Store(),
                            annotation=None,
                            type_comment=None)
                    ],
                    value=nodes)
            else:
                nodes.name = ctx.info.name

            if logging.has_verbosity(2):
                logging.log(2, 'Transformed %s:\n\n%s\n', fn, parser.unparse(nodes))

            factory = _PythonFnFactory(
                ctx.info.name, fn.__code__.co_freevars, self.get_extra_locals())
            factory.create(
                nodes, ctx.namer, future_features=ctx.info.future_features)
            self._cache[fn][cache_subkey] = factory

transformed_fn = factory.instantiate(
    globals_=fn.__globals__,
    closure=fn.__closure__ or (),
    defaults=fn.__defaults__,
    kwdefaults=getattr(fn, '__kwdefaults__', None))
exit((transformed_fn, factory.module, factory.source_map))
