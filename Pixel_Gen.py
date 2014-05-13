#Pixel Gen.py
import os, sys
from PIL import Image
from sets import Set

def get_color_index(pixel, palatte):
	for i in range(0, len(palatte)):
		if (palatte[i] == pixel):
			return i

def gen_data(sprite, delimiter):
	palatte = Set([])
	for i in range(0, len(sprite)):
		palatte.add(sprite[i])
	palatte = list(palatte)
	print palatte
	current = sprite[0]
	count = 0
	total = 0
	print '================================================='
	sys.stdout.write("[")
	for i in range(0, len(sprite)):
		if (i == len(sprite)-1):
			sys.stdout.write("[" + str(sprite[i][0]) + ", " + str(sprite[i][1]) + ", " + str(sprite[i][2]) + ", " + str(sprite[i][3]) + "]]\n")
		else:
			sys.stdout.write("[" + str(sprite[i][0]) + ", " + str(sprite[i][1]) + ", " + str(sprite[i][2]) + ", " + str(sprite[i][3]) + "], ")
		# if (get_color_index(sprite[i], palatte) == get_color_index(current, palatte)):
		# 	count = count + 1
		# else:
		# 	print "color " + str(get_color_index(current, palatte)) + ", " + str(count) + " times\n"
		# 	current = sprite[i]
		# 	total = total + count
		# 	count = 1
	# print "color" + str(get_color_index(current, palatte)) + ", " + str(count) + " times\n"
	# total = total + count
	# print "total: " + str(total)

def main():
	# Input checking
	if (len(sys.argv) != 3):
	    print "Usage: File_encypt.py input_filename pixel_delimiter"
	    sys.exit()
	delimiter = sys.argv[2]
	input_filename = sys.argv[1]
	im = Image.open(input_filename)
	pix = im.load()
	size = im.size
	print size
	sprite = []
	for y in range(size[1]):
		for x in range (size[0]):
			pixel = pix[x,y]
			sprite.append(pixel)
			print (x,y)
			print pix[x,y]
	gen_data(sprite, delimiter)

main()