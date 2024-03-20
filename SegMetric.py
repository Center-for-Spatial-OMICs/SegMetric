# import necessary packages
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
from skimage.io import imread, imshow
import numpy as np
import pandas as pd
import scanpy as sc
import anndata as ad
import sys

# python SegMetric.py '01202023_S17-16194_A1_Scan1.tif' '01202023_S17-16194_A1_Scan1_StarDist.tif' 1000 500 6800

image_path = str(sys.argv[1])
mask_path = str(sys.argv[2])
niter = int(sys.argv[3])
sample_size = int(sys.argv[4])
mask_value_exclude = int(sys.argv[5])

images = imread(image_path)
DAPI_layer = images[0,:,:]

mask = imread(mask_path)
mask[mask == mask_value_exclude] = 0 # need to do this for StarDist because tissue thresholder is given the value of 6800
mask[mask != 0] = 1

# otsu thresholding binary image
thresh = threshold_otsu(DAPI_layer)
binary = DAPI_layer > thresh

counter = 1
arr_imagecov = []
arr_maskcov = []

while counter <= niter:
    # select a random sample
    height, width = binary.shape
    top_left_row = np.random.randint(0, height - sample_size + 1)
    top_left_col = np.random.randint(0, width - sample_size + 1)

    sampled_square = binary[top_left_row:top_left_row + sample_size, top_left_col:top_left_col + sample_size]
    # imshow(sampled_square)

    # count number of pixels
    imagecov = np.count_nonzero(sampled_square)/(np.shape(sampled_square)[0]*np.shape(sampled_square)[1])*100

    # look at cell segmentation using overlay mask
    sampled_mask = mask[top_left_row:top_left_row + sample_size, top_left_col:top_left_col + sample_size]
    # imshow(sampled_mask)

    # count number of pixels
    maskcov = np.count_nonzero(sampled_mask)/(np.shape(sampled_mask)[0]*np.shape(sampled_mask)[1])*100

    if (imagecov > 0) or (maskcov > 0):
        arr_imagecov.append(imagecov)
        arr_maskcov.append(maskcov)
        counter = counter + 1

fig, ax = plt.subplots(figsize = (8, 5))
ax.scatter(arr_imagecov, arr_maskcov, s=30, alpha=0.5, color='blue')
b, a = np.polyfit(arr_imagecov, arr_maskcov, deg=1)
xseq = np.linspace(0, np.maximum(arr_imagecov, arr_maskcov), num=1000)
ax.plot(xseq, a + b * xseq, color="k", lw=0.2)
plt.xlabel('Image Coverage')
plt.ylabel('Mask Coverage')
plt.title('Image Segmentation Correlation')
plt.legend()

r_squared = (np.corrcoef(arr_imagecov, arr_maskcov)[0, 1])**2
print(r_squared)

plt.text(0.05, 0.95, ('R^2: '+str(r_squared)), transform=ax.transAxes, fontsize=12, va='top', ha='left')

plt.savefig(mask_path.replace('.tif', '_corr'))