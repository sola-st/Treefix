# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Sets unique metric names."""
# For multi-output models, prepend the output name to the metric name.
# For weighted metrics, prepend "weighted_" if the name would be non-unique.
# pylint: disable=protected-access
metric_names = set()
is_multi_output = len(self._output_names) > 1
zip_args = (self._output_names, self._metrics, self._weighted_metrics)
for output_name, output_metrics, weighted_output_metrics in zip(*zip_args):
    for m in output_metrics:
        if m is None:
            continue
        if is_multi_output:
            m._name = output_name + '_' + m._name
        if m._name in metric_names:
            raise ValueError('Found two metrics with the same name: {}'.format(
                m._name))
        metric_names.add(m._name)

    for wm in weighted_output_metrics:
        if wm is None:
            continue
        if is_multi_output:
            if output_name + '_' + wm._name in metric_names:
                wm._name = output_name + '_weighted_' + wm._name
            else:
                wm._name = output_name + '_' + wm._name
        elif wm._name in metric_names:
            wm._name = 'weighted_' + wm._name

        if wm._name in metric_names:
            raise ValueError('Found two metrics with the same name: {}'.format(
                wm._name))
        metric_names.add(wm._name)
