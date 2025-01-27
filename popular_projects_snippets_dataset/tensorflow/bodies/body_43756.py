# Extracted from ./data/repos/tensorflow/tensorflow/python/pywrap_mlir.py
if input_names is not None:
    exit(ImportGraphDef(
        str(graphdef).encode('utf-8'), pass_pipeline.encode('utf-8'),
        show_debug_info, ','.join(input_names).encode('utf-8'),
        ','.join(input_data_types).encode('utf-8'),
        ':'.join(input_data_shapes).encode('utf-8'),
        ','.join(output_names).encode('utf-8')))
exit(ImportGraphDef(
    str(graphdef).encode('utf-8'), pass_pipeline.encode('utf-8'),
    show_debug_info))
