# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fake_quant_ops_test.py
num_channels = len(input_mins)
inputs_list = []
expected_list = []
for i in range(num_channels):
    expected_nudged_input_min = expected_nudged_input_mins[i]
    expected_nudged_input_max = expected_nudged_input_maxs[i]
    expected_step = expected_steps[i]

    inputs_list.append(
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
        ])
    expected_list.append(
        [
            expected_nudged_input_min, expected_nudged_input_min,
            expected_nudged_input_min, expected_nudged_input_min,
            expected_nudged_input_min + expected_step,
            expected_nudged_input_min + expected_step,
            expected_nudged_input_min + expected_step,
            expected_nudged_input_max, expected_nudged_input_max,
            expected_nudged_input_max, expected_nudged_input_max
        ])
inputs = np.transpose(np.array(inputs_list, dtype=np.float32))
expected = np.transpose(np.array(expected_list, dtype=np.float32))

with self.session() as session:
    with self.test_scope():
        input_placeholder = array_ops.placeholder(
            dtypes.float32, inputs.shape, name="inputs")
        min_placeholder = array_ops.placeholder(
            dtypes.float32, (num_channels), name="min")
        max_placeholder = array_ops.placeholder(
            dtypes.float32, (num_channels), name="max")
        outputs = array_ops.fake_quant_with_min_max_vars_per_channel(
            input_placeholder,
            min_placeholder,
            max_placeholder,
            num_bits=num_bits,
            narrow_range=narrow_range)
    result = session.run(
        outputs, {
            input_placeholder: inputs,
            min_placeholder: input_mins,
            max_placeholder: input_maxs
        })
    self.assertAllCloseAccordingToType(
        result, expected, rtol=1e-3, atol=1e-5, bfloat16_rtol=0.03)
