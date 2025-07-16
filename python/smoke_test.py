# Tests for kernelregression.py
# Tests use small bandwidth so that averaging between points is minimal, and expected behaviour is easier to see

from kernelregression import kernel_regression
import matplotlib.pyplot as plt

# Test 1 - linear regression. Expected behaviour - kernel regression should mimic linear regression
XI = [1, 2, 3, 4, 5]
YI = [1, 2, 3, 4, 5]
BW = [0.1, 0.1, 0.1, 0.1, 0.1]

x,mhat = kernel_regression(XI, YI, BW = BW)

# Test 2 - regression with repeated values (i.e. multiple y for a given x) - expected behaviour - kernel regression should go through mean of points
XI = [1, 2, 3, 4, 4]
YI = [1, 2, 3, 4, 1]
BW = [0.1, 0.1, 0.1, 0.1, 0.1]

x,mhat = kernel_regression(XI, YI, BW = BW)


# Test 3 - regression with repeated values and weighting - expeected behaviour - regression should be closer to points with higher weightings
XI = [1, 2, 3, 4, 4]
YI = [1, 2, 3, 4, 1]
BW = [0.1, 0.1, 0.1, 0.1, 0.1]
WI = [1, 1, 1, 1, 50]

x,mhat = kernel_regression(XI, YI, BW = BW, WI=WI)