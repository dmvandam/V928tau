# Best Fits
This file contains all the best fits used in the paper to show models for the stellar variation and the eclipse.
This is as follows:

### Stellar Variation
- m  - slope of the linear trend [L*/day]
- c  - y-intercept of the linear trend [L*]
- a1 - amplitude of the 1st sinusoid [L*] 
- a2 - amplitude of the 2nd sinusoid [L*] 
- a3 - amplitude of the 3rd sinusoid [L*] 
- a4 - amplitude of the 4th sinusoid [L*] 
- T1 - period of the 1st sinusoid [day] 
- T2 - period of the 2nd sinusoid [day] 
- T3 - period of the 3rd sinusoid [day] 
- T4 - period of the 4th sinusoid [day] 
- p1 - phase of the 1st sinusoid [rad] 
- a2 - phase of the 2nd sinusoid [rad] 
- a3 - phase of the 3rd sinusoid [rad] 
- a4 - phase of the 4th sinusoid [rad] 

Note that this model is defined as follows

    corr_time = time - time[0]
    line  = m * corr_time + c
    sine1 = a1 * np.sin(2 * np.pi * corr_time / T1 + p1)
    sine2 = a2 * np.sin(2 * np.pi * corr_time / T2 + p2)
    sine3 = a3 * np.sin(2 * np.pi * corr_time / T3 + p3)
    sine4 = a4 * np.sin(2 * np.pi * corr_time / T4 + p4)
    
    stellar_variation_model = line + sine1 + sine2 + sine3 + sine4


### Eclipse

Some things to note here are that the limb-darkening parameter is fixed at u = 0.7220.

- rdisk - disk radius [R*]
- redge - edge thickness [R*]
- b     - impact parameter [R*]
- inc   - inclination (0 = face-on, pi/2 = edge-on) [rad]
- tilt  - tilt (angle w.r.t. orbital path) [rad]
- vel   - transverse velocity [R*/day]
- dt    - time shift of eclipse minimum [day]
- taud  - opacity of the disk [-]
- taue  - opacity of the edge [-]

Above are all the parameters, but there are variations of the disk model.
1) Fuzzy Disk has all these parameters
2) Translucent Disk has: redge = 0 [R*], taue = 0
3) Opaque Disk has: redge = 0 [R*] ,taue = 0, taud = 1

The model is defined using pyPplusS.segment_models.LC_ringed()

    # planet position at the given times
    xp = (time - dt) * vel
    yp = b * np.ones_like(xp)
    # companion properties
    rp  = np.zeros_like(xp)
    ri  = 1e-16 * np.ones_like(xp)
    ro1 = rdisk * np.ones_like(xp)
    ro2 = (rdisk + redge) * np.ones_like(xp)
    # star: limb-darkening
    c2 = 0.7220 # u
    c1 = c3 = c4 = 0
    # calculate light curve of the disk then the edge then the combination
    lc_d = LC_ringed(rp, ri, ro1, xp, yp, inc, tilt, taud, c1, c2, c3, c4)
    if (redge != 0.) and (taue != 0.):
        lc_e = LC_ringed(rp, ro1, ro2, xp, yp, inc, tilt, taue, c1, c2, c3, c4)
    else:
        lc_e = 1
    lc = lc_d + lc_e - 1

    eclipse_model = lc
