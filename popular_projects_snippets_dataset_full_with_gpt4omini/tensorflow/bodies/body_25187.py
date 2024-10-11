# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/matmul"
out = self._registry.dispatch_command("node_info", ["-a", node_name])

test_attr_key_val_pairs = [("transpose_a", "b: false"),
                           ("transpose_b", "b: false"),
                           ("T", "type: DT_DOUBLE")]
if test_util.IsMklEnabled():
    test_attr_key_val_pairs.append(("_kernel", 's: "MklNameChangeOp"'))

assert_node_attribute_lines(
    self,
    out,
    node_name,
    _matmul_op_name(),
    self._main_device, [("Identity", "simple_mul_add/u/read"),
                        ("Identity", "simple_mul_add/v/read")], [],
    [("AddV2", "simple_mul_add/add"), ("AddV2", "simple_mul_add/add")], [],
    attr_key_val_pairs=test_attr_key_val_pairs)
check_main_menu(
    self,
    out,
    list_tensors_enabled=True,
    list_inputs_node_name=node_name,
    print_tensor_node_name=node_name,
    list_outputs_node_name=node_name)
