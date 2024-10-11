# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_aot_compile.py
"""Returns a Makefile string with variables for using XLA binary object files.

  Attempts to identify the right include header paths when run from either
  an installed TensorFlow pip package, or from bazel run.

  Args:
    output_prefix: A string containing the output prefix for the XLA AOT
      compiled header + object files.

  Returns:
    A string containing a filled out `_XLA_MAKEFILE_TEMPLATE`.
  """
sysconfig = _sysconfig_module()
output_dir, _ = os.path.split(output_prefix)
if sysconfig:
    tensorflow_includes = _shlex_quote(sysconfig.get_include())
else:
    # Try hard to find the real source directory if this is a local bazel run.
    if os.path.islink(__file__):
        this_file = __file__
        while os.path.islink(this_file):
            this_file = os.readlink(this_file)
        base = os.path.realpath(
            os.path.join(os.path.dirname(this_file), *([os.path.pardir] * 3)))
    else:
        try:
            base = test.test_src_dir_path('')
        except KeyError:  # Can't find TEST_SRCDIR in environment path.
            base = os.path.realpath(
                os.path.join(os.path.dirname(__file__), *([os.path.pardir] * 3)))
    expected_header = os.path.join(
        base, 'tensorflow', 'compiler', 'tf2xla', 'xla_compiled_cpu_function.h')
    if not os.path.exists(expected_header):
        logging.error(
            'Could not find includes path.  Missing file: {}'
            .format(expected_header))
    tensorflow_includes = base

exit(_XLA_MAKEFILE_TEMPLATE.format(
    tensorflow_includes=tensorflow_includes,
    compiled_dir=_shlex_quote(output_dir),
    cxx_flags='-D_GLIBCXX_USE_CXX11_ABI={}'.format(
        versions.CXX11_ABI_FLAG)))
