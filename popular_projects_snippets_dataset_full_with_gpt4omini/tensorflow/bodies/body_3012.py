# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/regression_tests/compile_and_run_test.py
filename = _TEST_FILE_NAME.value
if not os.path.isabs(filename):
    filename = os.path.join(resource_loader.get_data_files_path(), filename)
with gfile.GFile(filename, mode='r') as f:
    mlir_function = f.read()
    arg_attrs = []
    with ir.Context() as ctx:
        ctx.allow_unregistered_dialects = True
        module = ir.Module.parse(mlir_function)
        func = module.body.operations[0]
        function_type = ir.FunctionType(
            ir.TypeAttr(func.attributes[_FUNCTION_TYPE_NAME]).value)
        function_name = ir.StringAttr(func.attributes['sym_name']).value
        # If the function has arguments, we expect argument attributes.
        entry_block = func.regions[0].blocks[0]
        if entry_block.arguments:
            self.assertIn(_ARG_ATTRIBUTES_NAME, func.attributes)
            arg_attrs = ir.ArrayAttr(func.attributes[_ARG_ATTRIBUTES_NAME])
    logging.info(f'processing {filename}')
    start = time.perf_counter()
    compiled = jitrt.compile(
        mlir_function,
        function_name,
        tf_jitrt.Specialization.ENABLED,
        vectorize=_VECTORIZE.value)
    end = time.perf_counter()
    logging.info(f'compiled {filename} in {end-start:0.4f} seconds')
    np.random.seed(_INPUT_DATA_SEED.value)
    args = []
    for arg_attr in arg_attrs:
        attr_dict = ir.DictAttr(arg_attr)
        if _SHAPE_VALUE_ATTRIBUTE_NAME in attr_dict:
            shape_value_attr = ir.DenseIntElementsAttr(
                attr_dict[_SHAPE_VALUE_ATTRIBUTE_NAME])
            shape_value = np.array(list(shape_value_attr)).astype(np.int32)
            args.append(shape_value)
        elif _STATIC_TYPE_ATTRIBUTE_NAME in attr_dict:
            static_type = ir.TypeAttr(
                attr_dict[_STATIC_TYPE_ATTRIBUTE_NAME]).value
            shaped_type = ir.ShapedType(static_type)
            np_element_type = CompileAndRunTest.mlir_type_to_np_type(
                shaped_type.element_type)
            arg = np.random.uniform(
                -10000.0, 10000.0, size=shaped_type.shape).astype(np_element_type)
            args.append(arg)
    self.assertEqual(len(args), len(arg_attrs))
    start = time.perf_counter()
    result = jitrt.execute(compiled, args)
    end = time.perf_counter()
    logging.info(f'executed {filename} in {end-start:0.4f} seconds')
    if _COMPARE_WITH_TENSORFLOW.value:
        start = time.perf_counter()
        expected = tfrt_fallback.run_tfrt_fallback(mlir_function, function_name,
                                                   args)
        end = time.perf_counter()
        logging.info(
            f'executed {filename} via tfrt fallback in {end-start:0.4f} seconds'
        )
        if len(function_type.results) > 1:
            # If there is more than one result, we need to iterate manually,
            # otherwise np.testing.assert_allclose will complain if not all
            # results have equal size.
            self.assertEqual(len(result), len(expected))
            for res, expect in zip(result, expected):
                np.testing.assert_allclose(res, expect, rtol=1e-5, atol=1e-5)
        else:
            np.testing.assert_allclose(result, expected, rtol=1e-5, atol=1e-5)
