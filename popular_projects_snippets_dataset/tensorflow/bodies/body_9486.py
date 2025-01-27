# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/sysconfig.py
"""Returns the compilation flags for compiling with TensorFlow.

  The returned list of arguments can be passed to the compiler for compiling
  against TensorFlow headers. The result is platform dependent.

  For example, on a typical Linux system with Python 3.7 the following command
  prints `['-I/usr/local/lib/python3.7/dist-packages/tensorflow/include',
  '-D_GLIBCXX_USE_CXX11_ABI=1', '-DEIGEN_MAX_ALIGN_BYTES=64']`

  >>> print(tf.sysconfig.get_compile_flags())

  Returns:
    A list of strings for the compiler flags.
  """
flags = []
flags.append('-I%s' % get_include())
flags.append('-D_GLIBCXX_USE_CXX11_ABI=%d' % _CXX11_ABI_FLAG)
cxx_version_flag = None
if _CXX_VERSION == 201103:
    cxx_version_flag = '--std=c++11'
elif _CXX_VERSION == 201402:
    cxx_version_flag = '--std=c++14'
elif _CXX_VERSION == 201703:
    cxx_version_flag = '--std=c++17'
elif _CXX_VERSION == 202002:
    cxx_version_flag = '--std=c++20'
if cxx_version_flag:
    flags.append(cxx_version_flag)
flags.append('-DEIGEN_MAX_ALIGN_BYTES=%d' %
             pywrap_tf_session.get_eigen_max_align_bytes())
exit(flags)
