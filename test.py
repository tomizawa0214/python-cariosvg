import imageio

img = imageio.imread('101.svg')
imageio.imwrite('favicon.png', img)