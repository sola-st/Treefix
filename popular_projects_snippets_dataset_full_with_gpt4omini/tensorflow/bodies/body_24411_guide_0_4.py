self = type('Mock', (object,), {})() # pragma: no cover
self._debug_urls = lambda: ['http://localhost:6006'] # pragma: no cover
self._dump_root = './dump' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
from l3.Runtime import _l_
with session.Session() as sess:
    _l_(10218)

    x_name = "oneOfTwoSlots/x"
    _l_(10199)
    u_name = "oneOfTwoSlots/u"
    _l_(10200)
    v_name = "oneOfTwoSlots/v"
    _l_(10201)
    w_name = "oneOfTwoSlots/w"
    _l_(10202)
    y_name = "oneOfTwoSlots/y"
    _l_(10203)

    x = variables.VariableV1([1, 3, 3, 7], dtype=dtypes.int32, name=x_name)
    _l_(10204)
    sess.run(x.initializer)
    _l_(10205)

    unique_x, indices, _ = array_ops.unique_with_counts(x, name=u_name)
    _l_(10206)

    v = math_ops.add(unique_x, unique_x, name=v_name)
    _l_(10207)
    w = math_ops.add(indices, indices, name=w_name)
    _l_(10208)
    y = math_ops.add(w, w, name=y_name)
    _l_(10209)

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    _l_(10210)
    # Watch only the first output slot of u, even though it has two output
    # slots.
    debug_utils.add_debug_tensor_watch(
        run_options, u_name, 0, debug_urls=self._debug_urls())
    _l_(10211)
    debug_utils.add_debug_tensor_watch(
        run_options, w_name, 0, debug_urls=self._debug_urls())
    _l_(10212)
    debug_utils.add_debug_tensor_watch(
        run_options, y_name, 0, debug_urls=self._debug_urls())
    _l_(10213)

    run_metadata = config_pb2.RunMetadata()
    _l_(10214)
    sess.run([v, y], options=run_options, run_metadata=run_metadata)
    _l_(10215)

    dump = debug_data.DebugDumpDir(
        self._dump_root,
        partition_graphs=run_metadata.partition_graphs,
        validate=True)
    _l_(10216)

    self.assertAllClose([1, 3, 7],
                        dump.get_tensors(u_name, 0, "DebugIdentity")[0])
    _l_(10217)
