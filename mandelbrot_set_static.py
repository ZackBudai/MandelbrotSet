## Author: Zack Budai
## Date: 22 Dec 2022

import numpy as np # import the numpy library for numerical operations
import matplotlib.pyplot as plt # import the matplotlib library for plotting

def mandelbrot(c, maxiter):
    """
    Calculate the value of the Mandelbrot set for a given complex number c.
    maxiter: maximum number of iterations to perform
    Returns the number of iterations it took for the absolute value of z to become greater than 2,
    or maxiter if it did not become greater than 2 after maxiter iterations.
    """
    z = c # initialize z to the value of c
    for n in range(maxiter): # loop through the specified number of iterations
        if abs(z) > 2: # if the absolute value of z is greater than 2
            return n # return the current iteration number
        z = z*z + c # update the value of z for the next iteration
    return maxiter # if the loop completes, return the maxiter value

def create_fractal(xmin, xmax, ymin, ymax, width, height, maxiter):
    """
    Generate a 2D array of values for the Mandelbrot set over a range of complex numbers.
    xmin, xmax: minimum and maximum values for the real part of the complex numbers
    ymin, ymax: minimum and maximum values for the imaginary part of the complex numbers
    width, height: number of points to sample in the real and imaginary directions
    maxiter: maximum number of iterations to perform in the mandelbrot() function
    Returns 3 1D arrays: real parts, imaginary parts, and Mandelbrot set values
    """
    r1 = np.linspace(xmin, xmax, width) # create an array of evenly spaced values for the real part
    r2 = np.linspace(ymin, ymax, height) # create an array of evenly spaced values for the imaginary part
    n3 = np.empty((width,height)) # create an empty 2D array to store the Mandelbrot set values
    for i in range(width): # loop through the real part values
        for j in range(height): # loop through the imaginary part values
            n3[i,j] = mandelbrot(r1[i] + 1j*r2[j], maxiter) # calculate the Mandelbrot set value for the complex number and store it in the array
    return (r1,r2,n3) # return the real parts, imaginary parts, and Mandelbrot set values

def plot_fractal(xmin, xmax, ymin, ymax, width=10, height=10, maxiter=256):
    """
    Plot the Mandelbrot set over a range of complex numbers.
    xmin, xmax: minimum and maximum values for the real part of the complex numbers
    ymin, ymax: minimum and maximum values for the imaginary part of the complex numbers
    width, height: width and height of the plot in inches
    maxiter: maximum number of iterations to perform in the mandelbrot() function
    """
    dpi = 72 # dots per inch for the plot
    img_width = dpi * width # width of the plot in pixels
    img_height = dpi * height # height of the plot in pixels
    x,y,z = create_fractal(xmin, xmax, ymin, ymax, img_width, img_height, maxiter)
    # generate the Mandelbrot set values over the specified range of complex numbers

    fig, ax = plt.subplots(figsize=(width, height), dpi=72) # create a new figure with the specified size and resolution
    ticks = np.arange(0,img_width,3*dpi) # create an array of tick positions for the x-axis
    x_ticks = xmin + (xmax-xmin)*ticks/img_width # convert the tick positions to values in the complex plane
    plt.xticks(ticks, x_ticks) # set the x-axis tick positions and labels
    y_ticks = ymin + (ymax-ymin)*ticks/img_width # convert the tick positions to values in the complex plane
    plt.yticks(ticks, y_ticks) # set the y-axis tick positions and labels
    ax.imshow(z.T, origin='lower', extent=[xmin, xmax, ymin, ymax])
    # plot the Mandelbrot set values as an image, with the origin at the lower left corner and the specified extent

plot_fractal(-2.0, 1.0, -1.0, 1.0) # call the plot_fractal function to generate the plot
plt.show() # display the plot


