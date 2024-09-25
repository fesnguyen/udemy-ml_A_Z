# prompt: load image state_idle.jpeg then neutralize it to 0,1 for CNN

import cv2
import numpy as np

import matplotlib.pyplot as plt
import tensorflow as tf
from keras.api.layers import MaxPooling2D

def load_and_neutralize_image(image_path):
  """Loads an image and neutralizes its pixel values to the range [0, 1].

  Args:
    image_path: The path to the image file.

  Returns:
    A NumPy array representing the neutralized image.
  """

  img = cv2.imread(image_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB if needed
  img = img.astype(np.float32) / 255.0  # Normalize to [0, 1]
  return img

def sharpening_convolution(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

    return cv2.filter2D(neutralized_image, -1, kernel)

def maxpooling_image(image):
    # Convert the sharpened image to a TensorFlow tensor
    sharpened_image_tensor = tf.convert_to_tensor(image, dtype=tf.float32)

    # Reshape the tensor to add a batch dimension and channel dimension (if needed)
    # For example, if your image is RGB:
    sharpened_image_tensor = tf.reshape(sharpened_image_tensor,
                                        [1, image.shape[0], image.shape[1], 3])

    # Apply max pooling
    pooled_image = tf.nn.max_pool2d(
        sharpened_image_tensor,
        ksize=[1, 2, 2, 1],  # Kernel size (2x2)
        strides=[1, 2, 2, 1],  # Strides (2x2)
        padding='SAME'  # Padding to maintain output size
    )

    # Convert the pooled image back to a NumPy array
    return pooled_image.numpy().squeeze()

def show_image(image):
  plt.imshow(image)
  plt.axis('off')  # Turn off axis labels
  plt.show()

# Load + neutralize image
image_path = 'data/e_0/state_0.png'
neutralized_image = load_and_neutralize_image(image_path)
print(neutralized_image.shape)
# show_image(neutralized_image)

# Convolution image
convolution_image = sharpening_convolution(neutralized_image)
# show_image(convolution_image)

pooled_image = maxpooling_image(convolution_image)
show_image(pooled_image)



