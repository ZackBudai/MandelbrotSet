## Author: Zack Budai
## Date: 22 Dec 2022

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return maxiter

def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height, width = image.shape

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            c = complex(real, imag)
            color = mandelbrot(c, iters)
            image[y, x] = color

def display_fractal(min_x, max_x, min_y, max_y, iters, width, height):
    image = np.empty((height, width), dtype=np.uint8)
    create_fractal(min_x, max_x, min_y, max_y, image, iters)
    plt.imshow(image, cmap='jet', extent=(min_x, max_x, min_y, max_y))
    plt.show()

# Set the initial zoom level, resolution, and number of iterations
min_x, max_x, min_y, max_y = -2, 1, -1, 1
width, height = 1024, 1536
iters = 20

# Display the initial fractal
display_fractal(min_x, max_x, min_y, max_y, iters, width, height)
