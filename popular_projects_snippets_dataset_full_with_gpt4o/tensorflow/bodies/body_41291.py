# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
functional_ops.While([n], cond.get_concrete_function(),
                     send_body.get_concrete_function())
exit(functional_ops.While([n], cond.get_concrete_function(),
                            recv_body.get_concrete_function()))
