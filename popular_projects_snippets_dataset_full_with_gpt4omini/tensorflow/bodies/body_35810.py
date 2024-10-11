# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    var_f = variables.Variable([2.0])
    add = var_f + 0.0
    radd = 1.0 + var_f
    sub = var_f - 1.0
    rsub = 1.0 - var_f
    mul = var_f * 10.0
    rmul = 10.0 * var_f
    div = var_f / 10.0
    rdiv = 10.0 / var_f
    lt = var_f < 3.0
    rlt = 3.0 < var_f
    le = var_f <= 2.0
    rle = 2.0 <= var_f
    gt = var_f > 3.0
    rgt = 3.0 > var_f
    ge = var_f >= 2.0
    rge = 2.0 >= var_f
    neg = -var_f
    abs_v = abs(var_f)

    var_i = variables.Variable([20])
    mod = var_i % 7
    rmod = 103 % var_i

    var_b = variables.Variable([True, False])
    and_v = operator.and_(var_b, [True, True])
    or_v = operator.or_(var_b, [False, True])
    xor_v = operator.xor(var_b, [False, False])
    invert_v = ~var_b

    rnd = np.random.rand(4, 4).astype("f")
    var_t = variables.Variable(rnd)
    slice_v = var_t[2, 0:0]

    var_m = variables.Variable([[2.0, 3.0]])
    matmul = var_m.__matmul__([[10.0], [20.0]])
    rmatmul = var_m.__rmatmul__([[10.0], [20.0]])

    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose([2.0], self.evaluate(add))
    self.assertAllClose([3.0], self.evaluate(radd))
    self.assertAllClose([1.0], self.evaluate(sub))
    self.assertAllClose([-1.0], self.evaluate(rsub))
    self.assertAllClose([20.0], self.evaluate(mul))
    self.assertAllClose([20.0], self.evaluate(rmul))
    self.assertAllClose([0.2], self.evaluate(div))
    self.assertAllClose([5.0], self.evaluate(rdiv))
    self.assertAllClose([-2.0], self.evaluate(neg))
    self.assertAllClose([2.0], self.evaluate(abs_v))
    self.assertAllClose([True], self.evaluate(lt))
    self.assertAllClose([False], self.evaluate(rlt))
    self.assertAllClose([True], self.evaluate(le))
    self.assertAllClose([True], self.evaluate(rle))
    self.assertAllClose([False], self.evaluate(gt))
    self.assertAllClose([True], self.evaluate(rgt))
    self.assertAllClose([True], self.evaluate(ge))
    self.assertAllClose([True], self.evaluate(rge))

    self.assertAllClose([6], self.evaluate(mod))
    self.assertAllClose([3], self.evaluate(rmod))

    self.assertAllClose([True, False], self.evaluate(and_v))
    self.assertAllClose([True, True], self.evaluate(or_v))
    self.assertAllClose([True, False], self.evaluate(xor_v))
    self.assertAllClose([False, True], self.evaluate(invert_v))

    self.assertAllClose(rnd[2, 0:0], self.evaluate(slice_v))

    self.assertAllClose([[80.0]], self.evaluate(matmul))
    self.assertAllClose([[20.0, 30.0], [40.0, 60.0]], self.evaluate(rmatmul))
