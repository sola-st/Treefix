# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fake_quant_ops_test.py
num_channels = len(input_mins)
inputs_list = []
gradients_list = []
expected_backprops_wrt_input_list = []
expected_backprops_wrt_min_list = []
expected_backprops_wrt_max_list = []
for i in range(num_channels):
    expected_nudged_input_min = expected_nudged_input_mins[i]
    expected_nudged_input_max = expected_nudged_input_maxs[i]
    expected_step = expected_steps[i]
    inputs = [
        expected_nudged_input_min - expected_step,
        expected_nudged_input_min - 0.01, expected_nudged_input_min,
        expected_nudged_input_min + 0.01,
        expected_nudged_input_min + expected_step - 0.01,
        expected_nudged_input_min + expected_step,
        expected_nudged_input_min + expected_step + 0.01,
        expected_nudged_input_max - 0.01, expected_nudged_input_max,
        expected_nudged_input_max + 0.01,
        expected_nudged_input_max + expected_step
    ]
    inputs_list.append(inputs)
    gradients_list.append(list(range(1, len(inputs) + 1)))
    expected_backprops_wrt_input_list.append(
        [0.0, 0.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 0.0, 0.0])
    expected_backprops_wrt_min_list.append(1.0 + 2.0)
    expected_backprops_wrt_max_list.append(10.0 + 11.0)

inputs = np.transpose(np.array(inputs_list, dtype=np.float32))
gradients = np.transpose(np.array(gradients_list, dtype=np.float32))
expected_backprops_wrt_input = np.transpose(np.array(
    expected_backprops_wrt_input_list, dtype=np.float32))
expected_backprops_wrt_min = np.array(
    expected_backprops_wrt_min_list, dtype=np.float32)
expected_backprops_wrt_max = np.array(
    expected_backprops_wrt_max_list, dtype=np.float32)

with self.session() as session:
    with self.test_scope():
        gradient_placeholder = array_ops.placeholder(
            dtypes.float32, gradients.shape, name="gradients")
        input_placeholder = array_ops.placeholder(
            dtypes.float32, inputs.shape, name="inputs")
        min_placeholder = array_ops.placeholder(
            dtypes.float32, (num_channels), name="min")
        max_placeholder = array_ops.placeholder(
            dtypes.float32, (num_channels), name="max")
        outputs = array_ops.fake_quant_with_min_max_vars_per_channel_gradient(
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
            min_placeholder: input_mins,
            max_placeholder: input_maxs
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
