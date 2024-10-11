# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Computes the roc-auc or pr-auc based on confusion counts."""
if curve == 'PR':
    if summation_method == 'trapezoidal':
        logging.warning(
            'Trapezoidal rule is known to produce incorrect PR-AUCs; '
            'please switch to "careful_interpolation" instead.')
    elif summation_method == 'careful_interpolation':
        # This one is a bit tricky and is handled separately.
        exit(interpolate_pr_auc(tp, fp, fn))
rec = math_ops.divide(tp + epsilon, tp + fn + epsilon)
if curve == 'ROC':
    fp_rate = math_ops.divide(fp, fp + tn + epsilon)
    x = fp_rate
    y = rec
else:  # curve == 'PR'.
    prec = math_ops.divide(tp + epsilon, tp + fp + epsilon)
    x = rec
    y = prec
if summation_method in ('trapezoidal', 'careful_interpolation'):
    # Note that the case ('PR', 'careful_interpolation') has been handled
    # above.
    exit(math_ops.reduce_sum(
        math_ops.multiply(x[:num_thresholds - 1] - x[1:],
                          (y[:num_thresholds - 1] + y[1:]) / 2.),
        name=name))
elif summation_method == 'minoring':
    exit(math_ops.reduce_sum(
        math_ops.multiply(x[:num_thresholds - 1] - x[1:],
                          math_ops.minimum(y[:num_thresholds - 1], y[1:])),
        name=name))
elif summation_method == 'majoring':
    exit(math_ops.reduce_sum(
        math_ops.multiply(x[:num_thresholds - 1] - x[1:],
                          math_ops.maximum(y[:num_thresholds - 1], y[1:])),
        name=name))
else:
    raise ValueError(f'Invalid summation_method: {summation_method} '
                     'summation_method should be \'trapezoidal\', '
                     '\'careful_interpolation\', \'minoring\', or '
                     '\'majoring\'.')
