# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
x_shapes = [
    [2, 2, 3],
    [4, 2, 3],
    [2, 4, 3],
    [2, 5, 3],
    [1000, 1, 3],
]
test_styles = [
    "all_random",
    "rg_same",
    "rb_same",
    "gb_same",
    "rgb_same",
]
for x_shape in x_shapes:
    for test_style in test_styles:
        x_np = np.random.rand(*x_shape) * 255.
        delta_h = np.random.rand() * 2.0 - 1.0
        if test_style == "all_random":
            pass
        elif test_style == "rg_same":
            x_np[..., 1] = x_np[..., 0]
        elif test_style == "rb_same":
            x_np[..., 2] = x_np[..., 0]
        elif test_style == "gb_same":
            x_np[..., 2] = x_np[..., 1]
        elif test_style == "rgb_same":
            x_np[..., 1] = x_np[..., 0]
            x_np[..., 2] = x_np[..., 0]
        else:
            raise AssertionError("Invalid test style: %s" % (test_style))
        y_np = self._adjustHueNp(x_np, delta_h)
        y_tf = self._adjustHueTf(x_np, delta_h)
        self.assertAllClose(y_tf, y_np, rtol=2e-5, atol=1e-4)
