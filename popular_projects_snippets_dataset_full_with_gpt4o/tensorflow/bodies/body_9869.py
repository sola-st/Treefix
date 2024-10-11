# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
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
