# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade.py
# Maps from a function name to a dictionary that describes how to
# map from an old argument keyword to the new argument keyword.
self.function_keyword_renames = {
    "tf.batch_matmul": {
        "adj_x": "adjoint_a",
        "adj_y": "adjoint_b",
    },
    "tf.count_nonzero": {
        "reduction_indices": "axis"
    },
    "tf.reduce_all": {
        "reduction_indices": "axis"
    },
    "tf.reduce_any": {
        "reduction_indices": "axis"
    },
    "tf.reduce_max": {
        "reduction_indices": "axis"
    },
    "tf.reduce_mean": {
        "reduction_indices": "axis"
    },
    "tf.reduce_min": {
        "reduction_indices": "axis"
    },
    "tf.reduce_prod": {
        "reduction_indices": "axis"
    },
    "tf.reduce_sum": {
        "reduction_indices": "axis"
    },
    "tf.reduce_logsumexp": {
        "reduction_indices": "axis"
    },
    "tf.expand_dims": {
        "dim": "axis"
    },
    "tf.argmax": {
        "dimension": "axis"
    },
    "tf.argmin": {
        "dimension": "axis"
    },
    "tf.reduce_join": {
        "reduction_indices": "axis"
    },
    "tf.sparse_concat": {
        "concat_dim": "axis"
    },
    "tf.sparse_split": {
        "split_dim": "axis"
    },
    "tf.sparse_reduce_sum": {
        "reduction_axes": "axis"
    },
    "tf.reverse_sequence": {
        "seq_dim": "seq_axis",
        "batch_dim": "batch_axis"
    },
    "tf.sparse_reduce_sum_sparse": {
        "reduction_axes": "axis"
    },
    "tf.squeeze": {
        "squeeze_dims": "axis"
    },
    "tf.split": {
        "split_dim": "axis",
        "num_split": "num_or_size_splits"
    },
    "tf.concat": {
        "concat_dim": "axis"
    },
}

# Mapping from function to the new name of the function
self.symbol_renames = {
    "tf.inv": "tf.reciprocal",
    "tf.contrib.deprecated.scalar_summary": "tf.summary.scalar",
    "tf.contrib.deprecated.histogram_summary": "tf.summary.histogram",
    "tf.listdiff": "tf.setdiff1d",
    "tf.list_diff": "tf.setdiff1d",
    "tf.mul": "tf.multiply",
    "tf.neg": "tf.negative",
    "tf.sub": "tf.subtract",
    "tf.train.SummaryWriter": "tf.summary.FileWriter",
    "tf.scalar_summary": "tf.summary.scalar",
    "tf.histogram_summary": "tf.summary.histogram",
    "tf.audio_summary": "tf.summary.audio",
    "tf.image_summary": "tf.summary.image",
    "tf.merge_summary": "tf.summary.merge",
    "tf.merge_all_summaries": "tf.summary.merge_all",
    "tf.image.per_image_whitening": "tf.image.per_image_standardization",
    "tf.all_variables": "tf.global_variables",
    "tf.VARIABLES": "tf.GLOBAL_VARIABLES",
    "tf.initialize_all_variables": "tf.global_variables_initializer",
    "tf.initialize_variables": "tf.variables_initializer",
    "tf.initialize_local_variables": "tf.local_variables_initializer",
    "tf.batch_matrix_diag": "tf.matrix_diag",
    "tf.batch_band_part": "tf.band_part",
    "tf.batch_set_diag": "tf.set_diag",
    "tf.batch_matrix_transpose": "tf.matrix_transpose",
    "tf.batch_matrix_determinant": "tf.matrix_determinant",
    "tf.batch_matrix_inverse": "tf.matrix_inverse",
    "tf.batch_cholesky": "tf.cholesky",
    "tf.batch_cholesky_solve": "tf.cholesky_solve",
    "tf.batch_matrix_solve": "tf.matrix_solve",
    "tf.batch_matrix_triangular_solve": "tf.matrix_triangular_solve",
    "tf.batch_matrix_solve_ls": "tf.matrix_solve_ls",
    "tf.batch_self_adjoint_eig": "tf.self_adjoint_eig",
    "tf.batch_self_adjoint_eigvals": "tf.self_adjoint_eigvals",
    "tf.batch_svd": "tf.svd",
    "tf.batch_fft": "tf.fft",
    "tf.batch_ifft": "tf.ifft",
    "tf.batch_fft2d": "tf.fft2d",
    "tf.batch_ifft2d": "tf.ifft2d",
    "tf.batch_fft3d": "tf.fft3d",
    "tf.batch_ifft3d": "tf.ifft3d",
    "tf.select": "tf.where",
    "tf.complex_abs": "tf.abs",
    "tf.batch_matmul": "tf.matmul",
    "tf.pack": "tf.stack",
    "tf.unpack": "tf.unstack",
    "tf.op_scope": "tf.name_scope",
}

self.change_to_function = {
    "tf.ones_initializer",
    "tf.zeros_initializer",
}

# Functions that were reordered should be changed to the new keyword args
# for safety, if positional arguments are used. If you have reversed the
# positional arguments yourself, this could do the wrong thing.
self.function_reorders = {
    "tf.split": ["axis", "num_or_size_splits", "value", "name"],
    "tf.sparse_split": ["axis", "num_or_size_splits", "value", "name"],
    "tf.concat": ["concat_dim", "values", "name"],
    "tf.svd": ["tensor", "compute_uv", "full_matrices", "name"],
    "tf.nn.softmax_cross_entropy_with_logits": [
        "logits", "labels", "dim", "name"
    ],
    "tf.nn.sparse_softmax_cross_entropy_with_logits": [
        "logits", "labels", "name"
    ],
    "tf.nn.sigmoid_cross_entropy_with_logits": ["logits", "labels", "name"],
    "tf.op_scope": ["values", "name", "default_name"],
}

# Warnings that should be printed if corresponding functions are used.
self.function_warnings = {
    "tf.reverse": (
        ast_edits.ERROR,
        "tf.reverse has had its argument semantics changed "
        "significantly. The converter cannot detect this reliably, so "
        "you need to inspect this usage manually.\n"),
}

self.module_deprecations = {}
