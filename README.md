# v928tau
This repository contains all the code to analyse the K2 light curve and the ground-based photometry.
This is separated into several notebooks and a certain file structure which is presented at the end of this README.

The steps for data analysis are as follows.

### 1) Stellar Variation
<em>Goal</em>: This section is used to model out the stellar variations seen in the clearly beating light curve of the <strong>K2</strong> data.
It does this by modeling out a linear trend, and then using Lomb-Scargle Periodograms to isolate four sinousoids, which are fitted using scipy.curve_fit().
This best fit from scipy.curve_fit() is used as an initial guess for an MCMC sampling method to give us the best fit model for the stellar variation.

<em>Result</em>: the model fits to within approximately 0.5% (excluding the eclipse).

### 2) Ground Stellar Variation
<em>Goal</em>: This section takes the model from (1) and fits it to the rest of the ground-based photometry to see if there is evidence that this pattern is long-lived.

<em>Result</em>: It is hard to tell because of the much larger photometric errors and whether or not the stellar activity would remain the same over the course of 10 years.

### 3) Period Folding
<em>Goal</em>: This section attempts to find a second eclipse in the 10 years of ground-based photometric data. Lots of periods are tested, the photometry is left unbinned and binned after subtracting the stellar variation model and then inspected by eye.

<em>Result</em>: Nothing conclusive, though some periods are deemed interesting as the photometry seems to line up to some extent. Note that this is expected as the stellar variation model is not extensively modelled over the course of the entire baseline.

### 4) Eclipse Modelling
<em>Goal</em>: This section attemps to find a circumplanetary disk solution to the eclipse. This is done with the help of <strong>pyPplusS</strong> a code package developed by Rein & Ofir 2019 (https://github.com/EdanRein/pyPplusS) and using an MCMC sampling method developed here. The models tested are a translucent single disk, an opaque single disk, and a two-component disk with the inner component more opaque than the outer edge.

#### a) Opaque Disk
Here we model an opaque disk (disk opacity = 1) with no edge component
#### b) Translucent Disk
Here we remove the disk opacity constraint above
#### c) Fuzzy Disk
Here we add a second component to the disk with an edge thickness and edge opacity


<em>Results</em>: Several solutions were found, the most interesting are discussed in the paper

### 5) Orbital Analysis
<em>Goal</em>: given the results from the previous sections we can determine some orbital parameters (the eccentricity, the periastron and apastron distance) and relate these to allowed masses and periods for the proposed companion around V928 Tau A or B.

<em>Results</em>: these are presented in the plots in "plots/parameters/"

### File Structure

v928tau : contains all the jupyter-notebooks 
  - Code : contains all the relevant functions for each of the notebooks
  - data : contains all the data files
      - photometry : light curves of K2 data
      - limb-darkening : contains all the data files from jktld for obtaining the limb-darkening parameter u
  - models : contains all the model data with mcmc backends (.h5) and best fits (.npy)
      - best_fits
      - backends (can be requested via e-mail)
  - plots : contains all the plots
      - paper : all plots used for the paper
      - ground_variation : has different folders for binsize and window size (xrange)
      - parameters : has the parameter maps around V928 Tau A+B (magnetic and standard)
      - period_folding : shows the plots used to determine interesting periods (can be requested via e-mail)
  - pyPplusS : code package by Rein & Ofir 2019 (https://github.com/EdanRein/pyPplusS)
