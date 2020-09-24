#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
############################# STELLAR VARIATIONS ##############################
###############################################################################

# This module contains all the functions necessary to model the stellar 
# variations from the K2 light curve of V928 Tau



########################
#%% STANDARD MODULES %%#
########################

import matplotlib.pyplot as plt
import numpy as np



#######################
#%% MODEL FUNCTIONS %%#
#######################

def line(time, slope, y_intercept):
    '''
    this is simply the a line function for scipy.optimize

    Parameters
    ----------
    time : array of floats
        contains time data for the light curve
    slope : float
        slope of the line
    y_intercept : float
        y-intercept of the line

    Returns
    -------
    trend : array of floats
        line that follows trend = slope * time_fixed + y_intercept
    '''
    time_fixed = time - time[0]
    trend = slope * time_fixed + y_intercept
    return trend

def mcmc_line(P, time):
    '''
    mcmc version of line function

    Parameters
    ----------
    P : list, tuple, array of floats
        contains parameters for line function
            m --> slope
            b --> y_intercept
    time : array of floats
        contains time data for the light curve
    
    Returns
    -------
    trend : array of floats
        line that follows trend = slope * time_fixed + y_intercept
    '''
    m, b = P
    trend = line(time, m, b)
    return trend

def sine(time, amplitude, period, phase):
    '''
    function that returns a sinusoid based on the inputs

    Parameters
    ----------
    time : array of float
        contains time data for the light curve
    amplitude : float
        amplitude of the sine
    period : float
        period of the sine
    phase : float
        phase of the sine

    Returns
    -------
    trend : array of float
        sine with given input parameters
    '''
    time_fixed = time - time[0]
    trend = amplitude * np.sin(2 * np.pi * time_fixed / period + phase)
    return trend

def mcmc_sine(P, time):
    '''
    mcmc version of sine function

    Parameters
    ----------
    P : list, tuple, array of floats
        contains parameters for line function
            a --> amplitude
            T --> period
            p --> phase
    time : array of floats
        contains time data for the light curve
    
    Returns
    -------
    trend : array of floats
        sine with given input parameters
    '''
    a, T, p = P
    trend = sine(time, a, T, p)
    return trend

def two_sines(time, amplitude1, amplitude2, period1, period2, phase1, phase2):
    '''
    function that returns the sum of two sinusoids

    Parameters
    ----------
    time : array of float
        contains time data for the light curve
    amplitude1 : float
        amplitude of the 1st sinusoid
    amplitude2 : float
        amplitude of the 2nd sinuosid
    period1 : float
        period of the 1st sinusoid
    period2 : float
        period of the 2nd sinusoid
    phase1 : float
        phase of the 1st sinusoid
    phase2 : float
        phase of the 2nd sinusoid

    Returns
    -------
    trend : array of float
        addition of sinusoid 1 and 2
    '''
    sine1 = sine(time, amplitude1, period1, phase1)
    sine2 = sine(time, amplitude2, period2, phase2)
    trend = sine1 + sine2
    return trend

def mcmc_two_sines(P, time):
    '''
    mcmc version of sine function

    Parameters
    ----------
    P : list, tuple, array of floats
        contains parameters for line function
            a1 --> amplitude1
            a2 --> amplitude2
            T1 --> period1
            T2 --> period2
            p1 --> phase1
            p2 --> phase2
    time : array of floats
        contains time data for the light curve
    
    Returns
    -------
    trend : array of floats
        addition of sinusoid 1 and 2
    '''
    a1, a2, T1, T2, p1, p2 = P
    trend = two_sines(time, a1, a2, T1, T2, p1, p2)
    return trend

def stellar_variation_prior(P):
    '''
    gives the limit of the parameter space for the model

    Parameters
    ----------
    P : list, tuple, array of floats
        contains parameters of the model
            m --> slope of the line
            b --> intercept of the line
            a1-4 --> amplitudes of the sinusoids
            t1-4 --> periods of the sinusoids
            p1-4 --> phases of the sinusoids

    Returns
    -------
    prior : float
        0 if in parameter space, - infinity if outside
    '''
    m, b, a1, a2, a3, a4, t1, t2, t3, t4, p1, p2, p3, p4 = P
    ml, mu = (-0.1, 0.1)
    bl, bu = (0.9, 1.1)
    al, au = (-0.05, 0.05)
    tl, tu = (0, 4)
    pl, pu = (0, 2*np.pi)
    if ((ml<=m<=mu) and (bl<=b<=bu) and (al<=a1<=au) and (al<=a2<=au) and
       (al<=a3<=au) and (al<=a4<=au) and (tl<=t1<=tu) and (tl<=t2<=tu) and
       (tl<=t3<=tu) and (tl<=t4<=tu) and (pl<=p1<=pu) and (pl<=p2<=pu) and
       (pl<=p3<=pu) and (pl<=p4<=pu)):
        prior = 0.0
    else:
        prior = -np.inf
    return prior

def stellar_variation_model(P, time):
    '''
    the 4 sinusoid + linear trend model of the stellar variation

    Parameters
    ----------
    P : list, tuple, array of floats
        contains the model parameters
            m --> slope of the line
            b --> intercept of the line
            a1-4 --> amplitudes of the sinusoids
            t1-4 --> periods of the sinusoids
            p1-4 --> phases of the sinusoids
    time : array
        contains time data for the light curve

    Returns
    -------
    model : array
        contains flux values for the light curve model
    '''
    m, b, a1, a2, a3, a4, T1, T2, T3, T4, p1, p2, p3, p4 = P
    trend = line(time, m, b)
    sine1 = sine(time, a1, T1, p1)
    sine2 = sine(time, a2, T2, p2)
    sine3 = sine(time, a3, T3, p3)
    sine4 = sine(time, a4, T4, p4)
    model = trend + sine1 + sine2 + sine3 + sine4
    return model

