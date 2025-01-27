# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/complex_div_test.py
for dtype in self.complex_types:
    # Test division by 0 scenarios.
    self._testBinary(
        gen_math_ops.real_div,
        np.array([
            complex(1, 1),
            complex(1, np.inf),
            complex(1, np.nan),
            complex(np.inf, 1),
            complex(np.inf, np.inf),
            complex(np.inf, np.nan),
            complex(np.nan, 1),
            complex(np.nan, np.inf),
            complex(np.nan, np.nan),
            complex(-np.inf, np.nan),
        ],
                 dtype=dtype),
        np.array([
            0 + 0j,
            0 + 0j,
            0 + 0j,
            0 + 0j,
            0 + 0j,
            0 + 0j,
            0 + 0j,
            0 + 0j,
            0 + 0j,
            0.0 + 0j,
        ],
                 dtype=dtype),
        expected=np.array([
            complex(np.inf, np.inf),
            complex(np.inf, np.inf),
            complex(np.inf, np.nan),
            complex(np.inf, np.inf),
            complex(np.inf, np.inf),
            complex(np.inf, np.nan),
            complex(np.nan, np.inf),
            complex(np.nan, np.inf),
            complex(np.nan, np.nan),
            complex(-np.inf, np.nan),
        ],
                          dtype=dtype))

    # Test division with finite numerator, inf/nan denominator.
    self._testBinary(
        gen_math_ops.real_div,
        np.array([
            1 + 1j,
            1 + 1j,
            1 + 1j,
            1 + 1j,
            1 + 1j,
            1 + 1j,
            1 + 1j,
            1 + 1j,
            1 + 1j,
        ],
                 dtype=dtype),
        np.array(
            [
                complex(1, np.inf),
                complex(1, np.nan),
                complex(np.inf, 1),
                complex(np.inf, np.inf),  # C++ and Python diverge here.
                complex(np.inf, np.nan),  # C++ and Python diverge here.
                complex(np.nan, 1),
                complex(np.nan, np.inf),  # C++ and Python diverge here.
                complex(np.nan, -np.inf),  # C++ and Python diverge here.
                complex(np.nan, np.nan),
            ],
            dtype=dtype),
        expected=np.array(
            [
                (1 + 1j) / complex(1, np.inf),
                (1 + 1j) / complex(1, np.nan),
                (1 + 1j) / complex(np.inf, 1),
                complex(0 + 0j),  # C++ and Python diverge here.
                complex(0 + 0j),  # C++ and Python diverge here.
                (1 + 1j) / complex(np.nan, 1),
                complex(0 + 0j),  # C++ and Python diverge here.
                complex(0 - 0j),  # C++ and Python diverge here.
                (1 + 1j) / complex(np.nan, np.nan),
            ],
            dtype=dtype))

    # Test division with inf/nan numerator, infinite denominator.
    self._testBinary(
        gen_math_ops.real_div,
        np.array([
            complex(1, np.inf),
            complex(1, np.nan),
            complex(np.inf, 1),
            complex(np.inf, np.inf),
            complex(np.inf, np.nan),
            complex(np.nan, 1),
            complex(np.nan, np.inf),
            complex(np.nan, np.nan),
            complex(np.nan, -np.inf),
        ],
                 dtype=dtype),
        np.array([
            1 + 1j,
            1 + 1j,
            1 + 1j,
            1 + 1j,
            1 + 1j,
            1 + 1j,
            1 + 1j,
            1 + 1j,
            -1 - 1j,
        ],
                 dtype=dtype),
        expected=np.array(
            [
                complex(np.inf, np.inf),  # C++ and Python diverge here.
                complex(1 / np.nan) / (1 + 1j),
                complex(np.inf / 1) / (1 + 1j),
                complex(np.inf, -np.nan),  # C++ and Python diverge here.
                complex(np.inf, -np.inf),  # C++ and Python diverge here.
                complex(np.nan / 1) / (1 + 1j),
                complex(np.inf, np.inf),  # C++ and Python diverge here.
                complex(np.nan / np.nan) / (1 + 1j),
                complex(np.inf, np.inf),  # C++ and Python diverge here.
            ],
            dtype=dtype))
