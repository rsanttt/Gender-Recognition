import os
import numpy as np
import Image

globvar = 0

###########################################################################
# Slice an image in little NxM images 
def slice_image(image,N,M):
	k = 0
	im = Image.fromarray(np.uint8(image))
	imgwidth, imgheight = im.size
	width = imgwidth / N
	height = imgheight / M
	contadori = 0
	contadorj = 0
	for i in range(0,imgheight,height):
		for j in range(0,imgwidth,width):
			if contadorj >= N or contadori>=M:
				break
			if contadorj == (N-1):
				if contadori >= (M-1):
					box = (j, i, imgwidth, imgheight)
					crop_image(im,box)
					contadorj += 1
				else:
					box = (j, i, imgwidth, i+height)
					crop_image(im,box)
					contadorj += 1
			elif contadori >= (M-1):
				box = (j, i, j+width, imgheight)
				crop_image(im,box)
				contadorj += 1
			else:
				box = (j, i, j+width, i+height)
				crop_image(im,box) 
				a = im.crop(box)
				contadorj += 1
		contadorj = 0
		contadori += 1

###########################################################################
# Function that crop the image
def crop_image(image, box):

	global globvar
	globvar += 1
	print 'recorte: ', box
	#  crop image
	crop_image = image.crop(box)
	# After crop u can save the image or work with the croped image
	crop_image.save("IMG-%s.png" % globvar)
	# transform image to array and LBP
	img = crop_image.convert("L")
	img = (np.asarray(img, dtype=np.uint8))



def main():

	img = Image.open("example.png")
	img = img.convert("L")
	img = (np.asarray(img, dtype=np.uint8))
	slice_image(img,3,3)


if __name__ == "__main__":
	main()