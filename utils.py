import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def show_img(type): 
    if type == "scale":
        path1 = "/content/NordicWomenInSTEM/images/Height.png"
        path2 = "/content/NordicWomenInSTEM/images/Width.png"
     if type == "translate":
        path1 = "/content/NordicWomenInSTEM/images/moveX.png"
        path2 = "/content/NordicWomenInSTEM/images/moveY.png"
    f, ax = plt.subplots(2, 1, figsize=(5, 5))
    f.suptitle("From black and white to color")

    ax[0].imread(path1)
    ax[0].axis("off")

    ax[1].imread(path2)
    ax[1].axis("off")

def create_new_color(red, green, blue):
    plt.imshow([[(red, green, blue)]])
    plt.axis("off")
    plt.show()


def create_color(color, targetRed, targetGreen, targetBlue, red=255, green=255, blue=255):
    fontsize = 20
    f, ax = plt.subplots(1, 2, figsize=(5, 2))
    f.suptitle("Can you make " + color + "?")
    r = targetRed
    g = targetGreen
    b = targetBlue
    ax[0].imshow([[(r, g, b)]])
    plt.setp(ax[0].get_xticklabels(), visible=False)
    plt.setp(ax[0].get_yticklabels(), visible=False)
    ax[0].tick_params(axis='both', which='both', length=0)

    ax[1].imshow([[(red, green, blue)]])
    plt.setp(ax[1].get_xticklabels(), visible=False)
    plt.setp(ax[1].get_yticklabels(), visible=False)
    ax[1].tick_params(axis='both', which='both', length=0)
    plt.show()

    if (red == r and green == g and blue == b):
        congrats = plt.imread("images\congratulations.jpg")
        plt.imshow(congrats)
        plt.title("Wow, perfect! You got the exact color!")
        plt.axis('off')
        plt.show()


def create_yellow(red=255, green=255, blue=255):
    create_color("yellow", 255, 255, 0, red, green, blue)


def create_light_blue(red=255, green=255, blue=255):
    create_color("light blue", 0, 255, 255, red, green, blue)


def create_purple(red=255, green=255, blue=255):
    create_color("purple", 90, 0, 90, red, green, blue)


def create_orange(red=255, green=255, blue=255):
    create_color("orange", 230, 130, 30, red, green, blue)


def create_black(red=255, green=255, blue=255):
    create_color("black", 0, 0, 0, red, green, blue)


def plot_matrix_as_image(matrix):
    plt.figure(figsize=(16, 16))
    ax = sns.heatmap(matrix.astype(int), annot=True, cmap='gray', fmt="d")
    plt.show()


def from_grayscale_to_color(gray, img):
    fontsize = 20
    f, ax = plt.subplots(1, 2, figsize=(5, 2))
    f.suptitle("From black and white to color")

    ax[0].imshow(gray, cmap='gray')
    ax[0].axis("off")

    ax[1].imshow(img)
    ax[1].axis("off")


def separate_channels(img):
    fontsize = 5
    f, ax = plt.subplots(1, 4, figsize=(6, 2))
    img = np.asarray(img)

    ax[0].imshow(img[:, :, 0],  cmap='Reds')
    ax[0].set_title("Red image", fontsize=fontsize)
    ax[0].axis("off")

    ax[1].imshow(img[:, :, 1], cmap='Greens')
    ax[1].set_title("Green image", fontsize=fontsize)
    ax[1].axis("off")

    ax[2].imshow(img[:, :, 2], cmap='Blues')
    ax[2].set_title("Blue image", fontsize=fontsize)
    ax[2].axis("off")

    ax[3].imshow(img)
    ax[3].set_title("Combined channels", fontsize=fontsize)
    ax[3].axis("off")


def before_and_after(img, t_image):
    fontsize = 20
    f, ax = plt.subplots(1, 2, figsize=(10, 10))
    img = np.asarray(img)
    ax[0].imshow(img, cmap='gray')
    ax[0].set_title("Original image", fontsize=fontsize)
    ax[0].axis("off")

    ax[1].imshow(t_image,  cmap='Reds')
    ax[1].set_title("Transformed image", fontsize=fontsize)
    ax[1].axis("off")


def plot_points(points, newpoints, target_color):
    hull = ConvexHull(points)
    newhull = ConvexHull(newpoints)

    xRange = abs(np.concatenate((points[:, 0], newpoints[:, 0])))
    yRange = abs(np.concatenate((points[:, 1], newpoints[:, 1])))
    fig, ax = plt.subplots(ncols=1, figsize=(5, 5))

    ax.plot(points[:, 0], points[:, 1], '.', color='k')
    ax.plot(newpoints[:, 0], newpoints[:, 1], '.', color='k')
    for simplex in hull.simplices:
        ax.plot(newpoints[simplex, 0], newpoints[simplex, 1], 'b', alpha=0.3)
        ax.plot(points[simplex, 0], points[simplex, 1], 'y', alpha=0.3)
    ax.fill(points[hull.vertices, 0], points[hull.vertices, 1],
            color=target_color, label="GOAL")
    ax.fill(newpoints[newhull.vertices, 0], newpoints[newhull.vertices,
            1], color='b', label="Your square", alpha=0.3)
    maxAxis = np.maximum(xRange.max(), yRange.max())
    plt.ylim((maxAxis*-1)-1, maxAxis+1)
    plt.xlim((maxAxis*-1)-1, maxAxis+1)
    plt.hlines(y=0, xmin=(maxAxis*-1)-1, xmax=(maxAxis
                                               )+1, colors='gray', linestyles='--', lw=0.5)
    plt.vlines(x=0, ymin=(maxAxis*-1)-1, ymax=(maxAxis
                                               )+1, colors='gray', linestyles='--', lw=0.5)
    plt.legend(loc="upper right")
    plt.show()


def move_square(M=np.float32([[1, 0, 0],
                              [0, 1, 0],
                              [0, 0, 1]]), target=np.array([[0, 0], [0, 1], [1, 1], [1, 0]]),
                target_color="y"):
    newpoints = []
    points = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
    for point in points:
        newx = M[0, 0] * point[0] + M[0, 1] * point[1] + M[0, 2]
        newy = M[1, 0] * point[0] + M[1, 1] * point[1] + M[1, 2]
        newpoints.append([newx, newy])

    newpoints = np.array(newpoints)
    plot_points(target, newpoints, target_color)


def excercise1(M):
    target = np.array([[0, 0], [0, 3], [2, 3], [2, 0]])
    move_square(M, target, target_color='tomato')


def excercise2(M):
    target = np.array([[-3, -3], [-2, -3], [-3, -2], [-2, -2]])
    move_square(M, target, target_color='limegreen')


def excercise3(M):
    target = np.array([[2, -3], [6, -3], [2, -5], [6, -5]])
    move_square(M, target, target_color='gold')
