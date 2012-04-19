import unittest, mathgsl


class MathTest(unittest.TestCase):

  def test_eps(self):
    '''DBL_EPSILON = 2**-52
                   = 2.2204460492503131e-16
       Is it defined in some Python module?
    '''
    eps = 2**-52 
    a = 1 + eps
    b = a - 1
    self.assertEqual(b, eps)
    eps1 = 2**-53
    a1 = 1 + eps1
    b1 = a1 - 1
    self.assertEqual(b1, 0)
    self.assertNotEqual(b1, eps)
    
  
  def test_M_PI(self):
    self.assertAlmostEqual(mathgsl.t_M_PI(), 
	3.14159265358979323846, 16)
    #   3.1415926535897931  is the Python repr

  def test_M_E(self):
    self.assertAlmostEqual(mathgsl.t_M_E(),
	2.7182818284590452354, 16)

  def test_M_LOG2E(self):
    self.assertAlmostEqual(mathgsl.t_M_LOG2E(),
	1.4426950408889634074, 16)
	
  def test_M_LOG10E(self):
    self.assertAlmostEqual(mathgsl.t_M_LOG10E(),
        0.43429448190325182765, 17)

    
  def test_M_LN2(self):
    self.assertAlmostEqual(mathgsl.t_M_LN2(),
	0.69314718055994530942, 17)

  def test_M_PI_2(self):
    self.assertAlmostEqual(mathgsl.t_M_PI_2(),
      1.57079632679489661923, 16)

  def test_M_PI_4(self):
    self.assertAlmostEqual(mathgsl.t_M_PI_4(),
	0.78539816339744830962, 17)

  def test_M_1_PI(self):
    self.assertAlmostEqual(mathgsl.t_M_1_PI(),
	0.31830988618379067154, 17)

  def test_M_2_PI(self):
    self.assertAlmostEqual(mathgsl.t_M_2_PI(),
	0.63661977236758134308, 17)

  def test_M_2_SQRTPI(self):
    self.assertAlmostEqual(mathgsl.t_M_2_SQRTPI(),
	1.12837916709551257390, 16)

  def test_M_SQRT2(self):
    self.assertAlmostEqual(mathgsl.t_M_SQRT2(),
        1.41421356237309504880, 16)

  def test_M_SQRT1_2(self):
    self.assertAlmostEqual(mathgsl.t_M_SQRT1_2(),
	0.70710678118654752440, 17)

  def test_M_LNPI(self):
    self.assertAlmostEqual(mathgsl.t_M_LNPI(), 0, 17)

  def test_M_EULER(self):
    self.assertAlmostEqual(mathgsl.t_M_EULER(), 
	0.577215664901532860606512, 17) # A-S p3


  def test_isnan1(self):
    self.assertEqual(mathgsl.t_isnan1(), 1)

  def test_isnan2(self):
    self.assertEqual(mathgsl.t_isnan2(), 0)

  def test_isinf1(self):
    self.assertEqual(mathgsl.t_isinf1(), 1)
    
  def test_isinf2(self):
    self.assertEqual(mathgsl.t_isinf2(), -1)
    
  def test_isinf3(self):
    self.assertEqual(mathgsl.t_isinf3(), 0)
    
  def test_finite1(self):
    self.assertEqual(mathgsl.t_finite1(), 0)
    
  def test_finite2(self):
    self.assertEqual(mathgsl.t_finite2(), 1)
      
	
  def test_gsl_log1p(self):
    self.assertAlmostEqual(mathgsl.t_gsl_log1p(1.3),0, 15)

  def test_gsl_expm1(self):
    self.assertAlmostEqual(mathgsl.t_gsl_expm1(1.3),0, 16)

  def test_gsl_hypot(self):
    self.assertAlmostEqual(mathgsl.t_gsl_hypot(1.3,2.1),0, 16)

  def test_gsl_acosh(self):
    self.assertAlmostEqual(mathgsl.t_gsl_acosh(1.3),0, 16)

  def test_gsl_asinh(self):
    self.assertAlmostEqual(mathgsl.t_gsl_asinh(1.3),0, 16)

  def test_gsl_atanh(self):
    self.assertAlmostEqual(mathgsl.t_gsl_atanh(1.3),0, 16)

  def test_gsl_ldexp(self):
    self.assertAlmostEqual(mathgsl.t_gsl_ldexp(1.3),0, 16)

  def test_gsl_frexp(self):
    t = mathgsl.t_gsl_frexp()
    self.assertAlmostEqual(t[0],0.6, 16)
    self.assertEqual(t[1], -15)

  x = 1.3

  def test_gsl_pow_2(self):
    self.assertAlmostEqual(mathgsl.t_gsl_pow_2(self.x),0, 16)

  def test_gsl_pow_3(self):
    self.assertAlmostEqual(mathgsl.t_gsl_pow_3(self.x),0, 16)

  def test_gsl_pow_4(self):
    self.assertAlmostEqual(mathgsl.t_gsl_pow_4(self.x),0, 16)

  def test_gsl_pow_5(self):
    self.assertAlmostEqual(mathgsl.t_gsl_pow_5(self.x),0, 16)

  def test_gsl_pow_6(self):
    self.assertAlmostEqual(mathgsl.t_gsl_pow_6(self.x),0, 16)

  def test_gsl_pow_7(self):
    self.assertAlmostEqual(mathgsl.t_gsl_pow_7(self.x),0, 16)

  def test_gsl_pow_8(self):
    self.assertAlmostEqual(mathgsl.t_gsl_pow_8(self.x),0, 16)

  def test_gsl_pow_9(self):
    self.assertAlmostEqual(mathgsl.t_gsl_pow_9(self.x),0, 16)

  def test_GSL_SIGN(self):
    self.assertEqual(mathgsl.t_GSL_SIGN(1.3),1, 16)
    self.assertEqual(mathgsl.t_GSL_SIGN(-1.3),-1, 16)

  def test_GSL_IS_ODD(self):
    self.assertEqual(mathgsl.t_GSL_IS_ODD(8),0)
    self.assertEqual(mathgsl.t_GSL_IS_ODD(9),1)

  def test_GSL_IS_EVEN(self):
    self.assertEqual(mathgsl.t_GSL_IS_EVEN(8),1)
    self.assertEqual(mathgsl.t_GSL_IS_EVEN(9),0)

  def test_GSL_MAX(self):
    x = 3.1; y = 2.3
    self.assertAlmostEqual(mathgsl.t_GSL_MAX(x,y),x, 16)

  def test_GSL_MIN(self):
    x = 3.1; y = 2.3
    self.assertAlmostEqual(mathgsl.t_GSL_MIN(x,y),y, 16)

  def test_GSL_MAX_DBL(self):
    x = 3.1; y = 2.3
    self.assertAlmostEqual(mathgsl.t_GSL_MAX_DBL(x,y),x, 16)

  def test_GSL_MIN_DBL(self):
    x = 3.1; y = 2.3
    self.assertAlmostEqual(mathgsl.t_GSL_MIN_DBL(x,y),y, 16)

  def test_GSL_MAX_INT(self):
    x = 3; y = 2
    self.assertEqual(mathgsl.t_GSL_MAX_INT(x,y),x)

  def test_GSL_MIN_INT(self):
    x = 3; y = 2
    self.assertAlmostEqual(mathgsl.t_GSL_MIN_INT(x,y),y)

  def test_gsl_fcmp1(self):
    self.assertEqual(mathgsl.t_gsl_fcmp1(),1)
    
  def test_gsl_fcmp2(self):
    self.assertEqual(mathgsl.t_gsl_fcmp2(),0)

  def test_gsl_fcmp3(self):
    self.assertEqual(mathgsl.t_gsl_fcmp3(),1)
    
  def test_gsl_function(self):
    self.assertAlmostEqual(mathgsl.t_gsl_function(),0, 16)

  def test_GSL_FN_EVAL(self):
    self.assertAlmostEqual(mathgsl.t_GSL_FN_EVAL(),0, 16)


if __name__ == '__main__':
  unittest.main()
