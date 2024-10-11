# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fake_quant_ops_test.py
inputs = np.array(
    [
        expected_nudged_input_min - expected_step,
        expected_nudged_input_min - 0.01, expected_nudged_input_min,
        expected_nudged_input_min + 0.01,
        expected_nudged_input_min + expected_step - 0.01,
        expected_nudged_input_min + expected_step,
        expected_nudged_input_min + expected_step + 0.01,
        expected_nudged_input_max - 0.01, expected_nudged_input_max,
        expected_nudged_input_max + 0.01,
        expected_nudged_input_max + expected_step
    ],
    dtype=np.float32)
expected = np.array(
    [
        expected_nudged_input_min, expected_nudged_input_min,
        expected_nudged_input_min, expected_nudged_input_min,
        expected_nudged_input_min + expected_step,
        expected_nudged_input_min + expected_step,
        expected_nudged_input_min + expected_step,
        expected_nudged_input_max, expected_nudged_input_max,
        expected_nudged_input_max, expected_nudged_input_max
    ],
    dtype=np.float32)

with self.session() as session:
    with self.test_scope():
        input_placeholder = array_ops.placeholder(
            dtypes.float32, inputs.shape, name="inputs")
        outputs = array_ops.fake_quant_with_min_max_args(
            input_placeholder,
            min=input_min,
            max=input_max,
            num_bits=num_bits,
            narrow_range=narrow_range)
    result = session.run(outputs, {input_placeholder: inputs})
    self.assertAllCloseAccordingToType(
        result, expected, rtol=1e-3, atol=1e-5, bfloat16_rtol=0.03)
