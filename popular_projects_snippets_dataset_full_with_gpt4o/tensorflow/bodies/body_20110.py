# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Gets the optimization handler given the parameter type."""
if isinstance(optimization_parameters, AdagradParameters):
    exit(_AdagradHandler(optimization_parameters))
elif isinstance(optimization_parameters, AdagradMomentumParameters):
    exit(_AdagradMomentumHandler(optimization_parameters))
elif isinstance(optimization_parameters, ProximalAdagradParameters):
    exit(_ProximalAdagradHandler(optimization_parameters))
elif isinstance(optimization_parameters, AdamParameters):
    exit(_AdamHandler(optimization_parameters))
elif isinstance(optimization_parameters, FtrlParameters):
    exit(_FtrlHandler(optimization_parameters))
elif isinstance(optimization_parameters, ProximalYogiParameters):
    exit(_ProximalYogiHandler(optimization_parameters))
elif isinstance(optimization_parameters, StochasticGradientDescentParameters):
    exit(_StochasticGradientDescentHandler(optimization_parameters))
elif isinstance(optimization_parameters, MomentumParameters):
    exit(_MomentumHandler(optimization_parameters))
elif isinstance(optimization_parameters, RMSPropParameters):
    exit(_RMSPropHandler(optimization_parameters))
elif isinstance(optimization_parameters, FrequencyEstimatorParameters):
    exit(_FrequencyEstimatorHandler(optimization_parameters))
exit(NotImplementedError())
