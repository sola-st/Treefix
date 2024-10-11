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
gradients = np.arange(1, len(inputs) + 1, dtype=np.float32)
expected_backprops_wrt_input = np.array(
    [0.0, 0.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 0.0, 0.0],
    dtype=np.float32)
expected_backprops_wrt_min = 1.0 + 2.0
expected_backprops_wrt_max = 10.0 + 11.0

with self.session() as session:
    with self.test_scope():
        gradient_placeholder = array_ops.placeholder(
            dtypes.float32, gradients.shape, name="gradients")
        input_placeholder = array_ops.placeholder(
            dtypes.float32, inputs.shape, name="inputs")
        min_placeholder = array_ops.placeholder(dtypes.float32, (), name="min")
        max_placeholder = array_ops.placeholder(dtypes.float32, (), name="max")
        outputs = array_ops.fake_quant_with_min_max_vars_gradient(
            gradient_placeholder,
            input_placeholder,
            min_placeholder,
            max_placeholder,
            num_bits=num_bits,
            narrow_range=narrow_range)
    backprops_wrt_input, backprops_wrt_min, backprops_wrt_max = session.run(
        outputs, {
            gradient_placeholder: gradients,
            input_placeholder: inputs,
            min_placeholder: input_min,
            max_placeholder: input_max
        })
    self.assertAllCloseAccordingToType(
        backprops_wrt_input,
        expected_backprops_wrt_input,
        rtol=1e-3,
        atol=1e-5,
        bfloat16_rtol=0.03)
    self.assertAllCloseAccordingToType(
        backprops_wrt_min,
        expected_backprops_wrt_min,
        rtol=1e-3,
        atol=1e-5,
        bfloat16_rtol=0.03)
    self.assertAllCloseAccordingToType(
        backprops_wrt_max,
        expected_backprops_wrt_max,
        rtol=1e-3,
        atol=1e-5,
        bfloat16_rtol=0.03)
