# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
setattr(cls, "__eq__", cls._create_comparison_method(operator.eq))
setattr(cls, "__ne__", cls._create_comparison_method(operator.ne))
setattr(cls, "__lt__", cls._create_comparison_method(operator.lt))
setattr(cls, "__gt__", cls._create_comparison_method(operator.gt))
setattr(cls, "__le__", cls._create_comparison_method(operator.le))
setattr(cls, "__ge__", cls._create_comparison_method(operator.ge))
