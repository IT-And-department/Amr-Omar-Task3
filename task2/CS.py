from matplotlib import pyplot as plt
import numpy as np
from skimage import io

# Load the image
img = io.imread("C:/Users/amr/OneDrive/Desktop/task/ppp.jpg")

# Perform contrast stretching
S = img.copy()
S_flat = S.flatten()  # Flatten the array for element-wise operations

# Define the min and max intensity values for contrast stretching
min_intensity = 0
max_intensity = 255

# Apply contrast stretching
S_flat = np.clip(S_flat, 0, 255)
S_flat = (S_flat - S_flat.min()) * (max_intensity - min_intensity) / (S_flat.max() - S_flat.min()) + min_intensity

# Reshape the flattened array back to the original shape
S = S_flat.reshape(S.shape)

# Display the images
plt.subplot(1, 2, 1)
plt.imshow(img, cmap=plt.cm.gray)
plt.title("Original Image")
plt.subplot(1, 2, 2)
plt.imshow(S, cmap=plt.cm.gray)
plt.title("Contrast Stretched Image")
plt.show()
