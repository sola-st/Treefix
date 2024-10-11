import numpy as np # pragma: no cover

function = type('Mock', (object,), {})() # pragma: no cover
session_lib = type('Mock', (object,), {})() # pragma: no cover
NoRewriteSessionConfig = type('Mock', (object,), {})() # pragma: no cover
array_ops = type('Mock', (object,), {'placeholder': lambda dtype: np.array([], dtype=dtype)})() # pragma: no cover
dtypes = type('Mock', (object,), {'float32': np.float32})() # pragma: no cover
config_pb2 = type('Mock', (object,), {'RunMetadata': lambda: None, 'RunOptions': lambda **kwargs: None})() # pragma: no cover
self = type('Mock', (object,), {'assertTrue': lambda cond: None})() # pragma: no cover
InLabels = lambda labels, name: True # pragma: no cover
RunMetadataLabels = lambda run_metadata: ['_XlaCompile', '_XlaRun'] # pragma: no cover
math_ops = type('Mock', (object,), {'log': np.log})() # pragma: no cover

import numpy as np # pragma: no cover

function = type('Mock', (object,), {'Defun': lambda compiled: lambda f: f})() # pragma: no cover
session_lib = type('Mock', (object,), {})() # pragma: no cover
NoRewriteSessionConfig = type('Mock', (object,), {})() # pragma: no cover
array_ops = type('Mock', (object,), {'placeholder': lambda dtype: tf.placeholder(dtype)})() # pragma: no cover
config_pb2 = type('Mock', (object,), {'RunMetadata': lambda: None, 'RunOptions': lambda **kwargs: None})() # pragma: no cover
self = type('Mock', (object,), {'assertTrue': lambda cond: None})() # pragma: no cover
InLabels = lambda labels, name: True # pragma: no cover
RunMetadataLabels = lambda run_metadata: ['_XlaCompile', '_XlaRun'] # pragma: no cover
math_ops = type('Mock', (object,), {'log': np.log})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py

from l3.Runtime import _l_
@function.Defun(compiled=True)
def CompiledFunction(x):
    _l_(9701)

    aux = math_ops.log(x)
    _l_(9700)
    exit(aux)

with session_lib.Session(config=NoRewriteSessionConfig()) as sess:
    _l_(9713)

    x = array_ops.placeholder(dtypes.float32)
    _l_(9702)
    y = CompiledFunction(x)
    _l_(9703)

    # Run the cluster with lots of shape signatures, but in a way that it
    # isn't megamorphic (i.e. each shape signature sees a lot of executions).
    # Then check that the cluster has not been marked as megamorphic.

    for shape in range(10, 50):
        _l_(9706)

        for _ in range(0, 1000):
            _l_(9705)

            sess.run(y, feed_dict={x: [0.] * shape})
            _l_(9704)

    for _ in range(0, 10):
        _l_(9708)

        sess.run(y, feed_dict={x: [0.] * 60})
        _l_(9707)

    run_metadata = config_pb2.RunMetadata()
    _l_(9709)
    sess.run(
        y,
        feed_dict={x: [0.] * 60},
        run_metadata=run_metadata,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    _l_(9710)
    self.assertTrue(InLabels(RunMetadataLabels(run_metadata), "_XlaCompile"))
    _l_(9711)
    self.assertTrue(InLabels(RunMetadataLabels(run_metadata), "_XlaRun"))
    _l_(9712)
