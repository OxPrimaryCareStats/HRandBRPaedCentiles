# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 19:08:35 2025

@author: David Wong
conversion of kernel regression code from Susannah Fleming, 2009
"""

import numpy as np

def run_regression(csv_file):
    """
    This is a wrapper for kernel_regression that takes input from a csv file. Example csv file in repo
    
    Parameters
    ----------
    csv_file : location of the csv file

    Returns
    -------
    MHAT : ndarray (M,)
        Estimated values at interpolation points
    X : ndarray (M,)
        Interpolation points
    """
    mydata = np.genfromtxt(csv_file, delimiter=',')
    XI = mydata[1:, 0]
    YI = mydata[1:, 1]
    WI = mydata[1:, 2]
    mhat, x = kernel_regression(XI, YI, WI = WI)
    return mhat, x



def kernel_regression(XI, YI, X=None, BW=None, WI=None, hmultiplier=2, p=0, minBW=np.finfo(float).eps):
    """
    Kernel regression using Gaussian kernels with variable bandwidths and weights.

    Parameters:
    XI : ndarray (N,)
        Input data (x-values)
    YI : ndarray (N,)
        Input data (y-values)
    X : ndarray (M,), optional
        Interpolation points for regression
    BW : ndarray (N,), optional
        Bandwidths associated with data
    WI : ndarray (N,), optional
        Weights associated with data
    hmultiplier : float, optional
        Multiplier for bandwidth (default is 2)
        specifically, hmultiplier is the value of h (bandwidth when BW = 1)
    p : int, optional
        Model order (0 = Nadaraya-Watson, 1 = local linear)
    minBW : float, optional
        Minimum bandwidth value (default is machine epsilon)

    Returns:
    MHAT : ndarray (M,)
        Estimated values at interpolation points
    X : ndarray (M,)
        Interpolation points
    """
    
    XI = np.asarray(XI)
    YI = np.asarray(YI)
    N = XI.shape[0]
    # note that behavior is very slightly different to original script
    # this version does not allow a single integer for XI or YI
    

    if (YI.shape != XI.shape) | (YI.ndim != 1) | (XI.ndim != 1):
        raise ValueError("Input sizes don't match")

    if X is None:
        M = 100
        X = np.linspace(np.min(XI), np.max(XI), M)
    else:
        X = np.asarray(X)
        if X.ndim != 1:
            raise ValueError("Input sizes don't match")
        M = X.shape[0]

    if BW is None:
        BW = np.ones(N)
    else:
        BW = np.asarray(BW)
        if (BW.ndim != 1) | (BW.shape[0] != N):
            raise ValueError("Input sizes don't match")

    if WI is None:
        WI = np.ones(N)
    else:
        WI = np.asarray(WI)
        if (WI.ndim !=1) | (WI.shape[0] != N):
            raise ValueError("Input sizes don't match")

    if p == 0:
        print('default Nadayar-Watson estimator')
    elif p == 1:
        print('local linear estimator')

    # Enforce minimum bandwidth
    BW[BW < minBW] = minBW
    HI = BW * hmultiplier

    # matrices for doing calculation
    XImat = np.tile(XI[:, None], (1, M))
    YImat = np.tile(YI[:, None], (1, M))
    Xmat = np.tile(X[None, :], (N, 1))
    HImat = np.tile(HI[:, None], (1, M))
    WImat = np.tile(WI[:, None], (1, M))

    # (Gaussian) kernel will be reused in calculation
    Kh = (WImat / HImat) * (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((XImat - Xmat) / HImat) ** 2)

    if p == 0:
        numerat = np.sum(Kh * YImat, axis=0)
        denominat = np.sum(Kh, axis=0)
        MHAT = numerat / denominat
    elif p == 1:
        S0 = (1 / N) * np.sum(Kh, axis=0)
        S0mat = np.tile(S0,(N,1));
        S1 = (1 / N) * np.sum((XImat - Xmat) * Kh, axis=0)
        S1mat = np.tile(S1,(N,1));
        S2 = (1 / N) * np.sum(((XImat - Xmat) ** 2) * Kh, axis=0)
        S2mat = np.tile(S2,(N,1));
        
        numerat = (S2mat - np.tile(S1, (N, 1)) * (XImat - Xmat)) * Kh * YImat
        denominat = S2mat * S0mat - S1mat**2

        MHAT = (1 / N) * np.sum(numerat / denominat, axis=0)
    else:
        raise ValueError("Only model orders 0 and 1 are supported")

    return MHAT, X