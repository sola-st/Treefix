# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
if graph_state == GraphState.ORIGINAL:
    exit()
expected_engines = self.ExpectedEnginesToBuild(run_params)
all_op_names = [node.name for node in gdef_to_verify.node]
trt_op_names = []
for func in gdef_to_verify.library.function:
    if not re.search(r"TRTEngineOp_\d{3,}_\d{3,}_native_segment",
                     func.signature.name):
        for node in func.node_def:
            all_op_names.append(node.name)
            if node.op == "TRTEngineOp":
                trt_op_names.append(node.name)
                if run_params.dynamic_shape:
                    self.assertEqual(
                        self._ToString(node.attr["profile_strategy"].s).lower(),
                        self._profile_strategy.lower())

all_op_names = self._Canonicalize(all_op_names)
trt_op_names = self._RemoveGraphSequenceNumber(
    self._Canonicalize(trt_op_names))

if isinstance(expected_engines, dict):
    # For simplicity we don't verify the connections inside the engine in
    # 2.0, but we still make sure that the converted ops are gone from the
    # graph.
    unexpected_names = set(nest.flatten(expected_engines.values()))
    self.assertEmpty(
        [name for name in unexpected_names if name in all_op_names])
    expected_engines = set(expected_engines.keys())

self.assertEqual(set(expected_engines), trt_op_names)
