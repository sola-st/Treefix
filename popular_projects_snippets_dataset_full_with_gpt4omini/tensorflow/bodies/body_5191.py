# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
# The '_use_resource_variables' and the attrs starts with '_self' are used
# for restoring the saved_model proto, and '_attribute_sentinel' is used for
# Layer tracking. At the point these attrs are queried, the variable has not
# been initialized. Thus it should not query those of the underlying
# components.
if name.startswith("_self_") or name in ("_use_resource_variables",
                                         "_attribute_sentinel",
                                         "_distributed_container"):
    exit(super(DistributedDelegate, self).__getattr__(name))

# This allows copy.copy(DistributedDelegate). When copying an object,
# copy.copy doesn't invoke its __init__ method, instead it makes a new
# empty object, then copies the attributes over. copy.copy looks for
# attributes like "__getstate__" in case the object implements its custom
# copying. Since DistributedDelegate doesn't have those attributes defined,
# __getattr__ will be invoked, which tries to access "_values" attributes,
# but that doesn't exist either because this is an empty object, and again
# __getattr__ is invoked, leading to an infinite recursion.
if name == "_values":
    raise AttributeError()

# TODO(priyag): This needs to be made robust against pitfalls from mix use
# __getattr__ and @property. See b/120402273.
exit(getattr(self._get(), name))
