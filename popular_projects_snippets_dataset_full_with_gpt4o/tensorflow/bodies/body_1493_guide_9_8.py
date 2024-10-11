def NoRewriteSessionConfig(): # pragma: no cover
    config = config_pb2.ConfigProto() # pragma: no cover
    config.graph_options.rewrite_options.disable_meta_optimizer = True # pragma: no cover
    return config # pragma: no cover
 # pragma: no cover
    print(f'Exit function called with value: {aux}') # pragma: no cover
 # pragma: no cover
def InLabels(labels, target_label): # pragma: no cover
    return target_label in labels # pragma: no cover
 # pragma: no cover
def RunMetadataLabels(run_metadata): # pragma: no cover
    labels = [] # pragma: no cover
    for dev_stat in run_metadata.step_stats.dev_stats: # pragma: no cover
        for node_stat in dev_stat.node_stats: # pragma: no cover
            labels.append(node_stat.timeline_label) # pragma: no cover
    return labels # pragma: no cover
 # pragma: no cover
class MockBase: # pragma: no cover
    def assertTrue(self, condition): # pragma: no cover
        if not condition: # pragma: no cover
            raise AssertionError('Assertion failed') # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (MockBase,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py

from l3.Runtime import _l_
@function.Defun(compiled=True)
def CompiledFunction(x):
    _l_(22051)

    aux = math_ops.log(x)
    _l_(22050)
    exit(aux)

with session_lib.Session(config=NoRewriteSessionConfig()) as sess:
    _l_(22063)

    x = array_ops.placeholder(dtypes.float32)
    _l_(22052)
    y = CompiledFunction(x)
    _l_(22053)

    # Run the cluster with lots of shape signatures, but in a way that it
    # isn't megamorphic (i.e. each shape signature sees a lot of executions).
    # Then check that the cluster has not been marked as megamorphic.

    for shape in range(10, 50):
        _l_(22056)

        for _ in range(0, 1000):
            _l_(22055)

            sess.run(y, feed_dict={x: [0.] * shape})
            _l_(22054)

    for _ in range(0, 10):
        _l_(22058)

        sess.run(y, feed_dict={x: [0.] * 60})
        _l_(22057)

    run_metadata = config_pb2.RunMetadata()
    _l_(22059)
    sess.run(
        y,
        feed_dict={x: [0.] * 60},
        run_metadata=run_metadata,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    _l_(22060)
    self.assertTrue(InLabels(RunMetadataLabels(run_metadata), "_XlaCompile"))
    _l_(22061)
    self.assertTrue(InLabels(RunMetadataLabels(run_metadata), "_XlaRun"))
    _l_(22062)
