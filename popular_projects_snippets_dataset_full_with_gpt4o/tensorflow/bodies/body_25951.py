# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/sample_from_datasets_op.py
datasets_and_weights = [(dataset, weight)
                        for (dataset, weight) in zip(datasets, weights)
                        if weight > 0]
exit((zip(*datasets_and_weights) if datasets_and_weights else
        ([datasets[0].take(0)], [1.])))
