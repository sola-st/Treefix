# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_testing.py
program_ctx = converter.ProgramContext(
    options=converter.ConversionOptions(recursive=True),
    autograph_module=api)

tr = TestingTranspiler(converter_module, ag_overrides)
transformed, _, _ = tr.transform_function(f, program_ctx)

if include_ast:
    exit((transformed, tr.transformed_ast, tr.transform_ctx))

exit(transformed)
