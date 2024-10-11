class MockSelf: # pragma: no cover
    def _debug_urls(self): # pragma: no cover
        return ['file:///tmp/tfdbg_dumps'] # pragma: no cover
 # pragma: no cover
    _dump_root = '/tmp/tfdbg_dumps' # pragma: no cover
 # pragma: no cover
    def assertAllClose(self, a, b): # pragma: no cover
        assert np.allclose(a, b), f'{a} vs {b}' # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

class MockSelf: # pragma: no cover
    def _debug_urls(self): # pragma: no cover
        return ['file:///tmp/tfdbg_dumps'] # pragma: no cover
 # pragma: no cover
    _dump_root = '/tmp/tfdbg_dumps' # pragma: no cover
 # pragma: no cover
    def assertAllClose(self, a, b): # pragma: no cover
        assert np.allclose(a, b), f'{a} vs {b}' # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
debug_utils = type('debug_utils', (object,), {'add_debug_tensor_watch': lambda run_options, tensor_name, slot, debug_urls: None}) # pragma: no cover
debug_data = type('debug_data', (object,), {'DebugDumpDir': lambda dump_root, partition_graphs, validate: type('MockDebugDumpDir', (object,), {'get_tensors': lambda self, u_name, slot, identity: [[1, 3, 7]]})()}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
from l3.Runtime import _l_
with session.Session() as sess:
    _l_(22461)

    x_name = "oneOfTwoSlots/x"
    _l_(22442)
    u_name = "oneOfTwoSlots/u"
    _l_(22443)
    v_name = "oneOfTwoSlots/v"
    _l_(22444)
    w_name = "oneOfTwoSlots/w"
    _l_(22445)
    y_name = "oneOfTwoSlots/y"
    _l_(22446)

    x = variables.VariableV1([1, 3, 3, 7], dtype=dtypes.int32, name=x_name)
    _l_(22447)
    sess.run(x.initializer)
    _l_(22448)

    unique_x, indices, _ = array_ops.unique_with_counts(x, name=u_name)
    _l_(22449)

    v = math_ops.add(unique_x, unique_x, name=v_name)
    _l_(22450)
    w = math_ops.add(indices, indices, name=w_name)
    _l_(22451)
    y = math_ops.add(w, w, name=y_name)
    _l_(22452)

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    _l_(22453)
    # Watch only the first output slot of u, even though it has two output
    # slots.
    debug_utils.add_debug_tensor_watch(
        run_options, u_name, 0, debug_urls=self._debug_urls())
    _l_(22454)
    debug_utils.add_debug_tensor_watch(
        run_options, w_name, 0, debug_urls=self._debug_urls())
    _l_(22455)
    debug_utils.add_debug_tensor_watch(
        run_options, y_name, 0, debug_urls=self._debug_urls())
    _l_(22456)

    run_metadata = config_pb2.RunMetadata()
    _l_(22457)
    sess.run([v, y], options=run_options, run_metadata=run_metadata)
    _l_(22458)

    dump = debug_data.DebugDumpDir(
        self._dump_root,
        partition_graphs=run_metadata.partition_graphs,
        validate=True)
    _l_(22459)

    self.assertAllClose([1, 3, 7],
                        dump.get_tensors(u_name, 0, "DebugIdentity")[0])
    _l_(22460)
