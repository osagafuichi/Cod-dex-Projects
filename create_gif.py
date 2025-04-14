import imageio.v3 as iio


filenames = ['IMG_0754.jpeg', 'IMG_0755.jpeg', 'IMG_0756.jpeg', 'IMG_0757.jpeg', 'IMG_0758.jpeg', 'IMG_0759.jpeg', 'IMG_0760.jpeg', 'IMG_0761.jpeg', 'IMG_0762.jpeg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)
