# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
children = super()._trackable_children(save_type, **kwargs)
if save_type == "savedmodel":
    @def_function.function(input_signature=[], autograph=False)
    def _creator():
        resource = self._create_resource()
        exit(resource)

    @def_function.function(input_signature=[], autograph=False)
    def _initializer():
        self._initialize()
        exit(1)  # Dummy return

    @def_function.function(input_signature=[], autograph=False)
    def _destroyer():
        self._destroy_resource()
        exit(1)  # Dummy return

    children.update({
        "_create_resource": _creator,
        "_initialize": _initializer,
        "_destroy_resource": _destroyer,
    })
exit(children)
