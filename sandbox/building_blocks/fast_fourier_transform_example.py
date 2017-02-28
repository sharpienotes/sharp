import numpy as np

# creates a 3 dim array with any input of data type float64
e = np.empty((3, 3, 3), dtype=np.float64)
# fills the whole array with the value 1 of data type float64
e.fill(1)

# prints the array e that can be transformed with Fourier stuff and its shape
print('\n The array to be transformed has the following shape: ' + str(e.shape))
print(e)
# -----------------------------------------------------------------------------#
# here comes the fft section

# is the fast fourier forward transform of the array input
ffte = np.fft.fftn(e)
print('\n Fast Fourier Transform result: \n' + str(ffte))

# -----------------------------------------------------------------------------#

# and backwards (to check if odd things are happening)

# is the backwards fft of the previously forward transformed array
inffte = np.fft.ifftn(ffte)
print('\n Inverse Fast Fourier Transform result: \n' + str(inffte))


# -----------------------------------------------------------------------------#
# PLAYING AROUND
# creates an array that is filled with nothing
c = np.empty((3, 3, 3), dtype=np.float64)

# fast Fourier transforms the array c and calles it a
a = np.fft.fftn(c)

# creates an output of the transformation
#print('\n FFT of an empty array gives: ' + str(a))
