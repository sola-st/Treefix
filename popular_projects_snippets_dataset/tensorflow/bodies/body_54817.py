# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
if self.color == "smaller_tuple":
    exit((self.x_shape, self.x_dtype, self.y_shape, self.y_dtype))
elif self.color == "different_order":
    exit((self.y_shape, self.x_shape, self.y_dtype, self.color,
            self.x_dtype))

exit((self.x_shape, self.x_dtype, self.y_shape, self.y_dtype, self.color))
