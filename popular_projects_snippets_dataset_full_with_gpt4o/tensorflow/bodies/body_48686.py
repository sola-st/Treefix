# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Updates the state of per-output metrics."""
y_true = self._conform_to_outputs(y_pred, y_true)
sample_weight = self._conform_to_outputs(y_pred, sample_weight)

if not self._built:
    self.build(y_pred, y_true)

y_pred = nest.flatten(y_pred)
y_true = nest.flatten(y_true) if y_true is not None else []
sample_weight = nest.flatten(sample_weight)

zip_args = (y_true, y_pred, sample_weight, self._metrics,
            self._weighted_metrics)
for y_t, y_p, sw, metric_objs, weighted_metric_objs in zip(*zip_args):
    # Ok to have no metrics for an output.
    if (y_t is None or (all(m is None for m in metric_objs) and
                        all(wm is None for wm in weighted_metric_objs))):
        continue

    y_t, y_p, sw = match_dtype_and_rank(y_t, y_p, sw)
    mask = get_mask(y_p)
    sw = apply_mask(y_p, sw, mask)

    for metric_obj in metric_objs:
        if metric_obj is None:
            continue
        metric_obj.update_state(y_t, y_p, sample_weight=mask)

    for weighted_metric_obj in weighted_metric_objs:
        if weighted_metric_obj is None:
            continue
        weighted_metric_obj.update_state(y_t, y_p, sample_weight=sw)
