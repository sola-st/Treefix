# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_test.py
super(XLATestCase, self).__init__(method_name)
if 'XLA' in FLAGS.test_device:
    context.context().enable_xla_devices()

# Check if the mlir bridge has been explicitly enabled or disabled. If
# is_mlir_bridge_enabled() returns None, the user did not explictly enable
# or disable the bridge so do not update enable_mlir_bridge.
if test_util.is_mlir_bridge_enabled():
    context.context().enable_mlir_bridge = True
elif test_util.is_mlir_bridge_enabled() is not None:
    context.context().enable_mlir_bridge = False

self.device = FLAGS.test_device
self.has_custom_call = (self.device == 'XLA_CPU')

# Some tests (e.g. ftrl_ops) only work if the program goes through the
# _TPUCompileMLIR op. They will set this flag to True.
# TODO(kramm): Flip to true (and enable MLIR bridge) for more tests.
self.rewrite_ops_for_tpu = False

self._all_tf_types = set([
    dtypes.as_dtype(types_pb2.DataType.Value(name))
    for name in FLAGS.types.split(',')
])
self.int_tf_types = set([
    dtype for dtype in self._all_tf_types if dtype.is_integer
])
self._float_tf_types = set([
    dtype for dtype in self._all_tf_types if dtype.is_floating
])
self.complex_tf_types = set([
    dtype for dtype in self._all_tf_types if dtype.is_complex
])
self._numeric_tf_types = set(
    self.int_tf_types | self._float_tf_types | self.complex_tf_types)
self.quantized_tf_types = set(
    dtype for dtype in self._all_tf_types if dtype.is_quantized)

# Quantized types don't have a numpy equivalent, include them in
# all_tf_types but not in all_types.
# TODO(b/115960798): Parametrize tests on TF types instead of numpy types
# and remove all_types.
self._all_types = set(dtype.as_numpy_dtype
                      for dtype in self._all_tf_types
                      if not dtype.is_quantized)
self._int_types = set([dtype.as_numpy_dtype for dtype in self.int_tf_types])
self.signed_int_types = set(dtype.as_numpy_dtype
                            for dtype in self.int_tf_types
                            if not dtype.is_unsigned)
self.unsigned_int_types = set(dtype.as_numpy_dtype
                              for dtype in self.int_tf_types
                              if dtype.is_unsigned)
self._float_types = set(
    [dtype.as_numpy_dtype for dtype in self._float_tf_types])
self.complex_types = set([
    dtype.as_numpy_dtype for dtype in self.complex_tf_types
])
self._numeric_types = set(self._int_types | self._float_types
                          | self.complex_types)

# Parse the manifest file, if any, into a regex identifying tests to
# disable
# TODO(xpan): Make it text proto if it doesn't scale.
# Each line of the manifest file specifies an entry. The entry can be
# 1) TestNameRegex  // E.g. CumprodTest.* Or
# 2) TestName TypeName  // E.g. AdamOptimizerTest.testSharing DT_BFLOAT16
# The 1) disables the entire test. While 2) only filter some numeric types
# so that they are not used in those tests.
self.disabled_regex = None
self._method_types_filter = {}

if FLAGS.disabled_manifest is not None:
    with open(FLAGS.disabled_manifest, 'r') as manifest_file:
        disabled_regex, self._method_types_filter = (
            parse_disabled_manifest(manifest_file.read()))
        if disabled_regex:
            self.disabled_regex = re.compile(disabled_regex)

if FLAGS.tf_xla_flags is not None:
    os.environ['TF_XLA_FLAGS'] = FLAGS.tf_xla_flags
