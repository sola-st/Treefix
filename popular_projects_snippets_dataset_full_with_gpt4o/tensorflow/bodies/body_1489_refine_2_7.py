NoRewriteSessionConfig = type('NoRewriteSessionConfig', (object,), {}) # pragma: no cover

NoRewriteSessionConfig = lambda: tf.compat.v1.ConfigProto(allow_soft_placement=True) # pragma: no cover
self = type('Mock', (object,), {'assertTrue': lambda self, x: None, 'assertFalse': lambda self, x: None})() # pragma: no cover
InLabels = lambda run_metadata, label: True # pragma: no cover
RunMetadataLabels = lambda run_metadata: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py

from l3.Runtime import _l_
@function.Defun(compiled=True)
def CompiledFunction(x):
    _l_(22106)

    aux = math_ops.log(x)
    _l_(22105)
    exit(aux)

with session_lib.Session(config=NoRewriteSessionConfig()) as sess:
    _l_(22125)

    x = array_ops.placeholder(dtypes.float32)
    _l_(22107)
    y = CompiledFunction(x)
    _l_(22108)

    # The very first run of the cluster is always compiled (non-lazily).
    run_metadata_for_first_run = config_pb2.RunMetadata()
    _l_(22109)
    sess.run(
        y,
        feed_dict={x: [2., 10., 19., 77., 100.]},
        run_metadata=run_metadata_for_first_run,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    _l_(22110)
    self.assertTrue(
        InLabels(
            RunMetadataLabels(run_metadata_for_first_run), "_XlaCompile"))
    _l_(22111)
    self.assertTrue(
        InLabels(RunMetadataLabels(run_metadata_for_first_run), "_XlaRun"))
    _l_(22112)

    run_metadata_before_warmup = config_pb2.RunMetadata()
    _l_(22113)
    sess.run(
        y,
        feed_dict={x: [2., 10.]},
        run_metadata=run_metadata_before_warmup,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    _l_(22114)
    self.assertTrue(
        InLabels(
            RunMetadataLabels(run_metadata_before_warmup), "_XlaCompile"))
    _l_(22115)
    self.assertFalse(
        InLabels(RunMetadataLabels(run_metadata_before_warmup), "_XlaRun"))
    _l_(22116)

    # We compile when we see the same shape a second time.

    run_metadata_after_warmup = config_pb2.RunMetadata()
    _l_(22117)
    sess.run(
        y,
        feed_dict={x: [2., 10.]},
        run_metadata=run_metadata_after_warmup,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    _l_(22118)
    self.assertTrue(
        InLabels(RunMetadataLabels(run_metadata_after_warmup), "_XlaCompile"))
    _l_(22119)
    self.assertTrue(
        InLabels(RunMetadataLabels(run_metadata_after_warmup), "_XlaRun"))
    _l_(22120)

    run_metadata_for_new_shape = config_pb2.RunMetadata()
    _l_(22121)
    sess.run(
        y,
        feed_dict={x: [2., 10., 12.]},
        run_metadata=run_metadata_for_new_shape,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    _l_(22122)
    self.assertTrue(
        InLabels(
            RunMetadataLabels(run_metadata_for_new_shape), "_XlaCompile"))
    _l_(22123)
    self.assertFalse(
        InLabels(RunMetadataLabels(run_metadata_for_new_shape), "_XlaRun"))
    _l_(22124)
