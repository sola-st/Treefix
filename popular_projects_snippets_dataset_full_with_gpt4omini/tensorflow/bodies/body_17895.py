# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
matrices = random_ops.random_uniform([3, 4, 4])
diags = random_ops.random_uniform([3, 4])
bands = random_ops.random_uniform([3, 3, 4])

def loop_fn(i):
    matrix_i = array_ops.gather(matrices, i)
    diag_i = array_ops.gather(diags, i)
    results = [
        array_ops.matrix_set_diag(matrix_i, diag_i),
        array_ops.matrix_set_diag(matrices[0, ...], diag_i),
        array_ops.matrix_set_diag(matrix_i, diags[0, ...]),
    ]

    k = (-1, 1)
    band_i = array_ops.gather(bands, i)
    for align in ["RIGHT_LEFT", "LEFT_RIGHT"]:
        results.extend([
            array_ops.matrix_set_diag(matrix_i, band_i, k=k, align=align),
            array_ops.matrix_set_diag(
                matrices[0, ...], band_i, k=k, align=align),
            array_ops.matrix_set_diag(
                matrix_i, bands[0, ...], k=k, align=align)
        ])
    exit(results)

self._test_loop_fn(loop_fn, 3)
