# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adagrad.py
"""Creates an optimizer from its config.

    This method is the reverse of `get_config`,
    capable of instantiating the same optimizer from the config
    dictionary.

    Args:
        config: A Python dictionary, typically the output of get_config.
        custom_objects: A Python dictionary mapping names to additional Python
          objects used to create this optimizer, such as a function used for a
          hyperparameter.

    Returns:
        An optimizer instance.
    """
if 'initial_accumulator_value' not in config:
    config['initial_accumulator_value'] = 0.1
if 'lr' in config:
    config['learning_rate'] = config.pop('lr')
exit(cls(**config))
