import cv2 as cv
import numpy as np

img = cv.imread('week2/pic/cat.jpg', cv.IMREAD_GRAYSCALE)

# Define the Sobel X operator for edge detection in the horizontal direction
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

# Compute the frequency representation of the Sobel X operator using FFT (Fast Fourier Transform)
# The 's' parameter specifies the shape of the output array (img.shape in this case)
sobel_x_freq = np.fft.fft2(sobel_x, s=img.shape)

# Shift the zero frequency component to the center of the spectrum
sobel_x_freq_shifted = np.fft.fftshift(sobel_x_freq)

# Compute the frequency representation of the input img using FFT
image_freq = np.fft.fft2(img)

# Shift the zero frequency component to the center of the spectrum
image_freq_shifted = np.fft.fftshift(image_freq)

# Extract the real and imaginary components from the shifted img frequency spectrum
real = np.real(image_freq_shifted)
imagine = np.imag(image_freq_shifted)

# Calculate the magnitude of the frequency spectrum
mag = np.sqrt(real**2 + imagine**2)

# Apply logarithmic scaling to enhance visualization
mag = np.log(1 + mag)

# Normalize the magnitude img to the range [0, 255] for display purposes
mag = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

# Calculate the magnitude of the Sobel X operator frequency spectrum
sobel_x_magnitude = np.abs(sobel_x_freq_shifted)

# Multiply the shifted input img frequency spectrum by the Sobel X operator magnitude spectrum
filtered_image_x_freq_shifted = image_freq_shifted * sobel_x_magnitude

# Shift the zero frequency component back to the corners of the spectrum
filtered_image_x = np.fft.ifftshift(filtered_image_x_freq_shifted)

# Perform inverse FFT to get the filtered img in the spatial domain
filtered_image_x = np.fft.ifft2(filtered_image_x)

# Get the magnitude of the filtered img (remove any imaginary components)
filtered_image_x = np.abs(filtered_image_x)

# Convert the filtered img to an unsigned 8-bit integer format for display
filtered_image_x = np.uint8(filtered_image_x)

# Display the input grayscale img, the magnitude spectrum, the Sobel X magnitude spectrum,
# and the final filtered img using the Sobel X operator
cv.imshow("Input Image in Grayscale", np.uint8(img))
cv.imshow("Magnitude Spectrum", mag)
cv.imshow("Sobel X Magnitude Spectrum", sobel_x_magnitude)
cv.imshow("Sobel X Edge Detection", filtered_image_x)

# Wait for a key press and then close all open windows
cv.waitKey(0)
cv.destroyAllWindows()
