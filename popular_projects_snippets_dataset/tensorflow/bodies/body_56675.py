# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/generate_examples_lib.py
"""Generate examples for a test set.

  Args:
    options: Options containing information to generate examples.

  Raises:
    RuntimeError: if the test function cannot be found.
  """
_prepare_dir(options)

out = options.zip_to_output
# Some zip filenames contain a postfix identifying the conversion mode. The
# list of valid conversion modes is defined in
# generated_test_conversion_modes() in build_def.bzl.

if options.multi_gen_state:
    test_name = options.multi_gen_state.test_name
else:
    # Remove suffixes to extract the test name from the output name.
    test_name = re.sub(
        r"(_(|with-flex|forward-compat|edgetpu|mlir-quant))?(_xnnpack)?\.zip$",
        "",
        out,
        count=1)

test_function_name = "make_%s_tests" % test_name
test_function = get_test_function(test_function_name)
if test_function is None:
    raise RuntimeError("Can't find a test function to create %r. Tried %r" %
                       (out, test_function_name))
if options.make_forward_compat_test:
    future_date = datetime.date.today() + datetime.timedelta(days=30)
    with tf.compat.forward_compatibility_horizon(future_date.year,
                                                 future_date.month,
                                                 future_date.day):
        test_function(options)
else:
    test_function(options)
