####Scope
This repo could more or less be a gist however because having a test file is useful it was made a repository. The goal is to generate the needed information/copy-pastable code to redraw the given png in html5/javascript. Currently all it does it print out the color and how many times it is used sequentially before it changes. It reads left to right, top to bottom.

####Usage
From the command line the program expects an input .png filename and, while it is not currently necessary, a delimiter. The delimiter will be used once it is able to handle sprite map conversion.

This was written and tested on python 2.7.5 and requires PIL. To install PIL simply run

<code>pip install PIL</code>
####Using the Provided Test-file
To see the palatte and the pixels in order of the provided file, reading left to right, top to bottom, Run 

<code>python Pixel_Gen.py simple_test.png 40</code>