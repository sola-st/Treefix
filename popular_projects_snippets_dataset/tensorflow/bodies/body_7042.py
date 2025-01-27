# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
exit(combinations.NamedDistribution(
    name,
    _get_ps_strategy_creator(
        num_workers=num_workers,
        num_ps=num_ps,
        required_gpus=required_gpus,
        variable_partitioner=variable_partitioner),
    required_gpus=required_gpus,
    num_workers=num_workers,
    has_chief=True,
    num_ps=num_ps))
