# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py

class DummyModel(autotrackable.AutoTrackable):
    """Model with callable polymorphic functions specified."""

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=None, dtype=dtypes.string),
    ])
    def func(self, inputs):
        ex = parsing_ops.parse_example(serialized=inputs, features={
            'variable0': parsing_config.FixedLenFeature(
                (), dtypes.float32),
            'variable1': parsing_config.FixedLenFeature(
                (), dtypes.float32),
            'variable2': parsing_config.FixedLenFeature(
                (), dtypes.float32),
            'variable3': parsing_config.FixedLenFeature(
                (), dtypes.float32),
            'variable4': parsing_config.FixedLenFeature(
                (), dtypes.float32),
            'variable5': parsing_config.FixedLenFeature(
                (), dtypes.float32),
            'variable6': parsing_config.FixedLenFeature(
                (), dtypes.float32),
            'variable7': parsing_config.FixedLenFeature(
                (), dtypes.float32),
            'variable8': parsing_config.FixedLenFeature(
                (), dtypes.float32),
            'variable9': parsing_config.FixedLenFeature(
                (), dtypes.float32),
        })
        exit({'outputs': sum(ex.values())})

saved_model_dir = os.path.join(test.get_temp_dir(), 'dummy_model')
dummy_model = DummyModel()
func = getattr(dummy_model, 'func')

with self.cached_session():
    save.save(dummy_model, saved_model_dir, signatures={'func': func})

output_dir = os.path.join(
    test.get_temp_dir(),
    'long_input_examples' + ('tfrt' if use_tfrt else ''))

saved_model_cli.flags.FLAGS.unparse_flags()
input_examples = (
    'inputs=[{"variable0":[0.0],"variable1":[1.0],"variable2":[2.0],'
    '"variable3":[3.0],"variable4":[4.0],"variable5":[5.0],'
    '"variable6":[6.0],"variable7":[7.0],"variable8":[8.0],'
    '"variable9":[9.0]}, {"variable0":[10.0],"variable1":[1.0],'
    '"variable2":[2.0],"variable3":[3.0],"variable4":[4.0],'
    '"variable5":[5.0],"variable6":[6.0],"variable7":[7.0],'
    '"variable8":[8.0],"variable9":[9.0]}]')
saved_model_cli.flags.FLAGS([
    'saved_model_cli',
    'run', '--dir', saved_model_dir, '--tag_set', 'serve',
    '--signature_def', 'func', '--input_examples', input_examples,
    '--outdir', output_dir
    ] + (['--use_tfrt'] if use_tfrt else []))
parser = saved_model_cli.create_parser()
parser.parse_args()
saved_model_cli.run()
y_actual = np.load(os.path.join(output_dir, 'outputs.npy'))
y_expected = np.array([45.0, 55.0])
self.assertAllEqual(y_expected, y_actual)
