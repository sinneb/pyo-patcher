from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from pylab import *
import PIL
from PIL import Image, ImageOps
import wave, struct, sys
import glob, os

for file in os.listdir("./"):
    if file.endswith(".wav"):
        print(file)
        outputfile = file[:-4] + '.png'

        input_data = read(file)
        audio = input_data[1]

        fig=figure()
        ax=fig.add_axes((0,0,1,1))
        ax.set_axis_off()
        ax.plot(audio[0:600]/1000.0, color="black")
        fig.savefig(outputfile)

        img = Image.open(outputfile)
        img = img.resize((100, 40), PIL.Image.ANTIALIAS)
        img = ImageOps.expand(img,border=1,fill='black')
        img.save(outputfile)

# plt.axis('off')
# plt.plot(audio[0:600]/1000.0)
# #plt.show()
# plt.savefig('foo.png')