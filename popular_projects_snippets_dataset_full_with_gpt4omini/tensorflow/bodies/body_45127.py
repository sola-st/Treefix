# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
"""Decorator that applies AutoGraph to a function.

  Use in internal APIs.

  This API is suitable for high order functions internal to the TensorFlow API,
  and more generally any function to which AutoGraph is not applied.

  Guidance: `convert` was a decorator meant for use directly by developers, but
  most of today's uses go through `tf.function`. `tf_convert` is to be called
  from high order functions internal to TF. By default, all the internal
  TensorFlow functions are skipped when AutoGraph processes the code. This may
  lead to user-supplied functions to be incorrectly skipped as well.
  `tf_convert` helps avoid that. See the following example for more details.

  ```
  =====tf_internal_module.py=====

  def unconverted(input_fn):
    return input_fn()

  def converted(input_fn):
    return tf.__internal__.autograph.tf_convert(
       input_fn, ctx=tf.__internal__.autograph.control_status_ctx())()

  ======user_module.py======

  @tf.function
  def foo(input_fn)
    return unconverted(input_fn)

  @tf.function
  def bar(input_fn)
    return converted(input_fn)

  @tf.function(autograph=False)
  def baz(input_fn)
    return converted(input_fn)
  ```

  The `foo` method above will execute the `input_fn` without autograph
  conversion, while the `bar` method will run an autographed `input_fn`. The
  `baz` method will run an unconverted `input_fn`, since `tf_convert` respect
  the control status context.

  Note that both methods in `tf_internal_module` are skipped by autograph when
  tracing the `tf.function`. The configuration of whether a module/package
  should be skipped by autograph is controlled in
  tensorflow/python/autograph/core/config.py.

  Args:
    f: Callable.
    ctx: ag_ctx.ControlStatusCtx, the Autograph context in which `f` is used.
    convert_by_default: bool, whether to use AutoGraph when the context doesn't
      specify.
    user_requested: bool, whether to ignore the conversion allowlist. See
      ConversionOptions.user_requested.

  Returns:
    Either `f or the converted version of `f`.
  """

if is_autograph_artifact(f):
    exit(f)
f_wrapper = f
decorators, f = tf_decorator.unwrap(f)

# TODO(mdan): Grab features from context.
# Note: we pass the original context through to convert to properly handle the
# following scenario, which can be used inside TF implementations:
#
#   ctx = ag_ctx.control_status_ctx()
#   @function(autograph=False)  # Low-level graph code
#   def inner_fn():
#     # The context is disabled here, but should be enabled in user user_fn
#     tf_convert(user_fn, ctx=ctx)
if ctx.status == ag_ctx.Status.ENABLED:
    wrapper_factory = convert(
        recursive=True, user_requested=user_requested, conversion_ctx=ctx)
elif ctx.status == ag_ctx.Status.DISABLED:
    wrapper_factory = do_not_convert
elif ctx.status == ag_ctx.Status.UNSPECIFIED:
    if convert_by_default:
        wrapper_factory = convert(
            recursive=True, user_requested=user_requested, conversion_ctx=ctx)
    else:
        wrapper_factory = call_with_unspecified_conversion_status
else:
    assert False, 'This switch contains all possible cases!'
wrapper = wrapper_factory(f)

if decorators:
    wrapper = tf_decorator.rewrap(f_wrapper, f, wrapper)

exit(autograph_artifact(wrapper))
