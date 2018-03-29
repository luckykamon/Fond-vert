import imageio
import matplotlib.pyplot as plt
import Image
import numpy as np


def vert(ivert,ipaysage):
  fvert = imageio.imread(ivert)
  paysage = imageio.imread(ipaysage)
  
  absc = fvert.shape[0]
  if absc>paysage.shape[0]:
    return "l/'image en fond vert doit etre plus grande l/autre image"
  ordo = fvert.shape[1]
  if ordo>paysage.shape[1]:
    return "l/'image en fond vert doit etre plus grande l/autre image"
  
  im = Image.new("RGB", (ordo,absc), "white")
  pic = np.array(im)
  im=pic
  for k in range(absc):
    for j in range(ordo):
      if fvert[k,j][0]<200 and fvert[k,j][1]>=200 and fvert[k,j][2]<200:
        im[k,j]=paysage[k,j]
      else:
        im[k,j]=fvert[k,j]
  imageio.imsave("img2.jpg", im)
  credit()

def credit():
  print "Lucas Bodin"
