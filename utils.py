

import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.spatial import ConvexHull


def plot_matrix_as_image(matrix): 
    plt.figure(figsize = (16,16))
    ax = sns.heatmap(matrix.astype(int), annot=True,cmap='gray',fmt="d")
    plt.show()


def from_grayscale_to_color(gray, img):
    fontsize = 20 
    f, ax = plt.subplots(1,2, figsize=(5,2))
    f.suptitle("From black and white to color")
    
    ax[0].imshow(gray, cmap='gray')
    ax[0].axis("off")
    
    ax[1].imshow(img)
    ax[1].axis("off")



def separate_channels(img):
    fontsize = 5 
    f, ax = plt.subplots(1,4, figsize=(6,2))
    img = np.asarray(img)
    
    ax[0].imshow(img[:,:,0],  cmap='Reds')
    ax[0].set_title("Red image", fontsize=fontsize)
    ax[0].axis("off")

    ax[1].imshow(img[:,:,1], cmap='Greens')
    ax[1].set_title("Green image", fontsize=fontsize)
    ax[1].axis("off")

    ax[2].imshow(img[:,:,2], cmap='Blues')
    ax[2].set_title("Blue image", fontsize=fontsize)
    ax[2].axis("off")

    ax[3].imshow(img)
    ax[3].set_title("Combined channels", fontsize=fontsize)
    ax[3].axis("off")




def before_and_after(img, t_image):
    fontsize = 20
    f, ax = plt.subplots(1,2, figsize=(10,10))
    img = np.asarray(img)
    ax[0].imshow(img, cmap='gray')
    ax[0].set_title("Original image", fontsize=fontsize)
    ax[0].axis("off")
    
    ax[1].imshow(t_image,  cmap='Reds')
    ax[1].set_title("Transformed image", fontsize=fontsize)
    ax[1].axis("off")


def plot_points(points, newpoints): 
    hull = ConvexHull(points)
    newhull = ConvexHull(newpoints)

    xRange =  abs(np.concatenate((points[:,0], newpoints[:,0])))
    yRange =  abs(np.concatenate((points[:,1], newpoints[:,1])))
    fig, ax = plt.subplots(ncols=1, figsize=(5,5))

    ax.plot(points[:, 0], points[:, 1], '.', color='k')
    ax.plot(newpoints[:, 0], newpoints[:, 1], '.', color='k')
    for simplex in hull.simplices:
        ax.plot(newpoints[simplex, 0], newpoints[simplex, 1], 'b', alpha = 0.3)
        ax.plot(points[simplex, 0], points[simplex, 1], 'y', alpha = 0.3)
    ax.fill(points[hull.vertices, 0], points[hull.vertices, 1], color='y', label= "original")
    ax.fill(newpoints[newhull.vertices, 0], newpoints[newhull.vertices, 1], color='b', label= "transformed", alpha = 0.3)
    plt.ylim((np.max(yRange)*-1)-1, (np.max(yRange))+1)
    plt.xlim((np.max(xRange)*-1)-1, (np.max(xRange))+1)
    plt.hlines(y=0, xmin=(np.max(xRange)*-1)-1, xmax=(np.max(xRange))+1, colors='gray',linestyles='--', lw=0.5)
    plt.vlines(x=0, ymin=(np.max(yRange)*-1)-1, ymax=(np.max(yRange))+1, colors='gray',linestyles='--', lw=0.5)
    plt.legend(loc="upper right")
    plt.show()