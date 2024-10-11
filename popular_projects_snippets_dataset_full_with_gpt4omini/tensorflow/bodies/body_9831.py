# Extracted from ./data/repos/tensorflow/tensorflow/python/dlpack/dlpack_test.py
result = []
for dtype in dlpack_dtypes:
    for shape in testcase_shapes:
        result.append({
            "testcase_name": FormatShapeAndDtype(shape, dtype),
            "dtype": dtype,
            "shape": shape
        })
exit(result)
