.. module:: cupyx.scipy.signal

Signal processing (:mod:`cupyx.scipy.signal`)
=============================================

.. Hint:: `SciPy API Reference: Signal processing (scipy.signal) <https://docs.scipy.org/doc/scipy/reference/signal.html>`_

Convolution
-----------

.. autosummary::
   :toctree: generated/

   convolve
   correlate
   fftconvolve
   oaconvolve
   convolve2d
   correlate2d
   sepfir2d
   choose_conv_method
   correlation_lags


B-Splines
---------

.. autosummary::
   :toctree: generated/

   cspline1d
   qspline1d
   cspline1d_eval
   qspline1d_eval


Filtering
---------

.. autosummary::
   :toctree: generated/

   order_filter
   medfilt
   medfilt2d
   wiener
   symiirorder1
   symiirorder2
   lfilter
   lfiltic
   lfilter_zi
   filtfilt
   savgol_filter
   deconvolve
   sosfilt
   sosfilt_zi
   sosfiltfilt
   detrend
   hilbert
   hilbert2


Filter design
-------------

.. autosummary::
   :toctree: generated/

   bilinear
   bilinear_zpk
   findfreqs
   freqs
   freqs_zpk
   freqz
   freqz_zpk
   sosfreqz
   firls
   minimum_phase
   savgol_coeffs
   gammatone
   group_delay
   iirdesign
   iirfilter
   kaiser_atten
   kaiser_beta
   kaiserord
   unique_roots
   residue
   residuez
   invres
   invresz


Matlab-style IIR filter design
------------------------------

.. autosummary::
   :toctree: generated/

   butter
   buttord
   ellip
   ellipord
   cheby1
   cheb1ord
   cheby2
   cheb2ord
   iircomb
   iirnotch
   iirpeak


Low-level filter design functions
---------------------------------

.. autosummary::
   :toctree: generated/

   abcd_normalize


Chirp Z-transform and Zoom FFT
------------------------------

.. autosummary::
   :toctree: generated/

   czt
   zoom_fft
   CZT
   ZoomFFT
   czt_points


LTI representations
-------------------

.. autosummary::
   :toctree: generated/

   zpk2tf
   zpk2sos
   tf2zpk
   tf2sos
   tf2ss
   ss2tf
   sos2tf
   sos2zpk


Continuous-time linear systems
------------------------------

.. autosummary::
   :toctree: generated/

   lti
   StateSpace
   TransferFunction
   ZerosPolesGain
   lsim
   impulse
   step
   freqresp
   bode


Discrete-time linear systems
----------------------------

.. autosummary::
   :toctree: generated/

   dlti
   StateSpace
   TransferFunction
   ZerosPolesGain
   dlsim
   dimpulse
   dstep
   dfreqresp
   dbode


Peak finding
------------

.. autosummary::
   :toctree: generated/

   find_peaks
   peak_prominences
   peak_widths


Spectral analysis
-----------------

.. autosummary::
   :toctree: generated/

   lombscargle
