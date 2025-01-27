# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
self._raise_pss_error_if_eager()
super(ParameterServerStrategyV1, self).run(
    fn, args=args, kwargs=kwargs, options=options)
