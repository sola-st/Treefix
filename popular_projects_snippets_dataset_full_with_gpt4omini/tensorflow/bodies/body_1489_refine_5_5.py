function = type('Mock', (object,), {})() # pragma: no cover
session_lib = type('Mock', (object,), {})() # pragma: no cover
NoRewriteSessionConfig = type('Mock', (object,), {})() # pragma: no cover
array_ops = type('Mock', (object,), {'placeholder': staticmethod(lambda dtype: 'placeholder for ' + str(dtype))})() # pragma: no cover
dtypes = type('Mock', (object,), {'float32': 'float32'})() # pragma: no cover
config_pb2 = type('Mock', (object,), {'RunMetadata': type('Mock', (object,), {})(), 'RunOptions': type('Mock', (object,), {})()})() # pragma: no cover
self = type('Mock', (object,), {'assertTrue': lambda x: None, 'assertFalse': lambda x: None})() # pragma: no cover
InLabels = lambda labels, label: label in labels # pragma: no cover
RunMetadataLabels = lambda metadata: ['_XlaCompile', '_XlaRun'] # pragma: no cover

function = type('MockFunction', (object,), {'Defun': staticmethod(lambda compiled: lambda f: f)})() # pragma: no cover
NoRewriteSessionConfig = type('Mock', (object,), {})() # pragma: no cover
array_ops = type('Mock', (object,), {'placeholder': staticmethod(lambda dtype: 'placeholder for ' + str(dtype))})() # pragma: no cover
dtypes = type('Mock', (object,), {'float32': 'float32'})() # pragma: no cover
config_pb2 = type('Mock', (object,), {'RunMetadata': type('Mock', (object,), {}), 'RunOptions': type('Mock', (object,), {'FULL_TRACE': 1})})() # pragma: no cover
self = type('MockSelf', (object,), {'assertTrue': lambda self, x: print(f'True: {x}'), 'assertFalse': lambda self, x: print(f'False: {x}')})() # pragma: no cover
InLabels = lambda labels, label: label in labels # pragma: no cover
RunMetadataLabels = lambda metadata: ['_XlaCompile', '_XlaRun'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py

from l3.Runtime import _l_
@function.Defun(compiled=True)
def CompiledFunction(x):
    _l_(9816)

    aux = math_ops.log(x)
    _l_(9815)
    exit(aux)

with session_lib.Session(config=NoRewriteSessionConfig()) as sess:
    _l_(9835)

    x = array_ops.placeholder(dtypes.float32)
    _l_(9817)
    y = CompiledFunction(x)
    _l_(9818)

    # The very first run of the cluster is always compiled (non-lazily).
    run_metadata_for_first_run = config_pb2.RunMetadata()
    _l_(9819)
    sess.run(
        y,
        feed_dict={x: [2., 10., 19., 77., 100.]},
        run_metadata=run_metadata_for_first_run,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    _l_(9820)
    self.assertTrue(
        InLabels(
            RunMetadataLabels(run_metadata_for_first_run), "_XlaCompile"))
    _l_(9821)
    self.assertTrue(
        InLabels(RunMetadataLabels(run_metadata_for_first_run), "_XlaRun"))
    _l_(9822)

    run_metadata_before_warmup = config_pb2.RunMetadata()
    _l_(9823)
    sess.run(
        y,
        feed_dict={x: [2., 10.]},
        run_metadata=run_metadata_before_warmup,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    _l_(9824)
    self.assertTrue(
        InLabels(
            RunMetadataLabels(run_metadata_before_warmup), "_XlaCompile"))
    _l_(9825)
    self.assertFalse(
        InLabels(RunMetadataLabels(run_metadata_before_warmup), "_XlaRun"))
    _l_(9826)

    # We compile when we see the same shape a second time.

    run_metadata_after_warmup = config_pb2.RunMetadata()
    _l_(9827)
    sess.run(
        y,
        feed_dict={x: [2., 10.]},
        run_metadata=run_metadata_after_warmup,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    _l_(9828)
    self.assertTrue(
        InLabels(RunMetadataLabels(run_metadata_after_warmup), "_XlaCompile"))
    _l_(9829)
    self.assertTrue(
        InLabels(RunMetadataLabels(run_metadata_after_warmup), "_XlaRun"))
    _l_(9830)

    run_metadata_for_new_shape = config_pb2.RunMetadata()
    _l_(9831)
    sess.run(
        y,
        feed_dict={x: [2., 10., 12.]},
        run_metadata=run_metadata_for_new_shape,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    _l_(9832)
    self.assertTrue(
        InLabels(
            RunMetadataLabels(run_metadata_for_new_shape), "_XlaCompile"))
    _l_(9833)
    self.assertFalse(
        InLabels(RunMetadataLabels(run_metadata_for_new_shape), "_XlaRun"))
    _l_(9834)
