#################################################
# Hw1
#################################################

from cs112_f16_wk1 import assertEqual, assertAlmostEqual, lintAll, testAll
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Hw1 problems
#################################################

def fabricYards(inches):
    return 42
 
def fabricExcess(inches):
    return  42

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    return 42

def colorBlender(rgb1, rgb2, midpoints, n):
    return 42

def bonusFindIntRootsOfCubic(a, b, c, d):
    return 42

#################################################
# Hw1 Test Functions
#################################################

def testFabricYards():
    print('Testing fabricYards()... ', end='')
    assertEqual(fabricYards(0), 0)
    assertEqual(fabricYards(1), 1)
    assertEqual(fabricYards(35), 1)
    assertEqual(fabricYards(36), 1)
    assertEqual(fabricYards(37), 2)
    assertEqual(fabricYards(72), 2)
    assertEqual(fabricYards(73), 3)
    assertEqual(fabricYards(108), 3)
    assertEqual(fabricYards(109), 4)
    print('Passed.')
 
def testFabricExcess():
    print('Testing fabricExcess()... ', end='')
    assertEqual(fabricExcess(0), 0)
    assertEqual(fabricExcess(1), 35)
    assertEqual(fabricExcess(35), 1)
    assertEqual(fabricExcess(36), 0)
    assertEqual(fabricExcess(37), 35)
    assertEqual(fabricExcess(72), 0)
    assertEqual(fabricExcess(73), 35)
    assertEqual(fabricExcess(108), 0)
    assertEqual(fabricExcess(109), 35)
    print('Passed.')

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assertEqual(isRightTriangle(0, 0, 0, 3, 4, 0), True)
    assertEqual(isRightTriangle(1, 1.3, 1.4, 1, 1, 1), True)
    assertEqual(isRightTriangle(9, 9.12, 8.95, 9, 9, 9), True)
    assertEqual(isRightTriangle(0, 0, 0, math.pi, math.e, 0), True)
    assertEqual(isRightTriangle(0, 0, 1, 1, 2, 0), True)
    assertEqual(isRightTriangle(0, 0, 1, 2, 2, 0), False)
    assertEqual(isRightTriangle(1, 0, 0, 3, 4, 0), False)
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assertEqual(colorBlender(220020060, 189252201, 3, -1), None)
    assertEqual(colorBlender(220020060, 189252201, 3, 0), 220020060)
    assertEqual(colorBlender(220020060, 189252201, 3, 1), 212078095)
    assertEqual(colorBlender(220020060, 189252201, 3, 2), 205136131)
    assertEqual(colorBlender(220020060, 189252201, 3, 3), 197194166)
    assertEqual(colorBlender(220020060, 189252201, 3, 4), 189252201)
    assertEqual(colorBlender(220020060, 189252201, 3, 5), None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assertEqual(colorBlender(1000255, 255002128, 2, -1), None)
    assertEqual(colorBlender(1000255, 255002128, 2, 0), 1000255)
    assertEqual(colorBlender(1000255, 255002128, 2, 1), 86001213)
    assertEqual(colorBlender(1000255, 255002128, 2, 2), 170001170)
    assertEqual(colorBlender(1000255, 255002128, 2, 3), 255002128)
    print('Passed.')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    observed = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assertEqual(observed, actual)

def testBonusFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

#################################################
# Hw1 Main
#################################################

def main():
    lintAll() # check style rules
    testAll(
        testFabricYards,
        testFabricExcess,
        testIsRightTriangle,
        testColorBlender,
        # testBonusFindIntRootsOfCubic
    )

if __name__ == '__main__':
    main()
