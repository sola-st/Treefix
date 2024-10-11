# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
try:
    vars_at_start = self._template_store.variables()
    trainable_at_start = self._template_store.trainable_variables()
    if self._variables_created:
        result = self._func(*args, **kwargs)
    else:
        # The first time we run, restore variables if necessary (via
        # Trackable).
        with trackable_util.capture_dependencies(template=self):
            result = self._func(*args, **kwargs)

    if self._variables_created:
        # Variables were previously created, implying this is not the first
        # time the template has been called. Check to make sure that no new
        # trainable variables were created this time around.
        trainable_variables = self._template_store.trainable_variables()
        # If a variable that we intend to train is created as a side effect
        # of creating a template, then that is almost certainly an error.
        if len(trainable_at_start) != len(trainable_variables):
            raise ValueError(
                "Trainable variable created when calling a template "
                "after the first time, perhaps you used tf.Variable "
                "when you meant tf.get_variable: %s" % list(
                    object_identity.ObjectIdentitySet(trainable_variables) -
                    object_identity.ObjectIdentitySet(trainable_at_start)))

        # Non-trainable tracking variables are a legitimate reason why a new
        # variable would be created, but it is a relatively advanced use-case,
        # so log it.
        variables = self._template_store.variables()
        if len(vars_at_start) != len(variables):
            logging.info(
                "New variables created when calling a template after "
                "the first time, perhaps you used tf.Variable when you "
                "meant tf.get_variable: %s",
                list(
                    object_identity.ObjectIdentitySet(variables) -
                    object_identity.ObjectIdentitySet(vars_at_start)))
    else:
        self._variables_created = True
    exit(result)
except Exception as exc:
    # Reraise the exception, but append the original definition to the
    # trace.
    args = exc.args
    if not args:
        arg0 = ""
    else:
        arg0 = args[0]
    trace = "".join(
        _skip_common_stack_elements(self._stacktrace,
                                    traceback.format_stack()))
    arg0 = "%s\n\noriginally defined at:\n%s" % (arg0, trace)
    new_args = [arg0]
    new_args.extend(args[1:])
    exc.args = tuple(new_args)
    raise
