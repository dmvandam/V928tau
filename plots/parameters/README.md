# Parameters
This folder contains all the plots produced by orbital analysis. 
It shows the available masses and periods for the companion based on the results of the eclipse modelling.
The most particular parameter is the transverse velocity.

Of other significant importance is whether the companion orbits V928 Tau A or B (due to the radius) and whether we use the mass obtained from the standard or magnetic models.


### Restrictions

Some of the considerations are listed below:

1. the apastron passage must be less than 10% of the binary separation (3.2 au)

This is for stability of the orbit. 
If the companion exceeds this distance, the orbit would become unstable due to the binary (we assume a stable orbit).

2. the total disk radius must be less than 0.3 times the Hill radius

This is for stability of the disk.
If the disk is larger then the disk would fall apart after much fewer orbits around the star.
Note that we evaluate the Hill radius at periastron passage.

3. the mass of the companion must be less than the substellar mass limit (80 Mjup)

This is due to the spectral energy distribution / imaging.
If the companion were larger than 80 Mjup it would start glowing significantly causing it to be visible in high-resolution imaging (depending on its distance), but it would also have an influence on the SED.

### Notes

From these restrictions we see that the curve at the bottom of each parameter map is carved out by the Hill radius requirement.
We also see that the apastron passage requirement carves out the right side of the parameter map.

### Name structure

x_Yc.png

x is the parameter, which can be eccentricity (e), periastron passage (rp), apastron passage (rap), or Hill radius (rh).
Y is the star V928 Tau A or B
c is either the standard (std) or magnetic (mag) model of the host star.
