#Importing Libraries
import os
import cv2
import numpy as np


def countSkinNonSkinPixels(img_data, mask_data):

    for i in range(img_data.shape[0]):
        for j in range(img_data.shape[1]):
            pixel = img_data[i, j]
            mask_pixel = mask_data[i, j]

            # Check if the pixel in the mask is white (non-skin)
            if np.all(mask_pixel >= [250, 250, 250]):
                # Increment the count for non-skin pixels
                nonSkin[pixel[0], pixel[1], pixel[2]] += 1
                total_non_skin += 1
            else:
                skin[pixel[0], pixel[1], pixel[2]] += 1
                total_skin += 1

#Calculate Probability

def calcProbability():

  #print(total_skin + total_non_skin)
  for i in range(255):
    for j in range(255):
      for k in range(255):
        pcns = pcs = 0
        if total_skin != 0 and total_non_skin != 0:
          pcs = skin[i, j, k] / total_skin
          pcns = nonSkin[i, j, k] / total_non_skin

        #probability[i, j, k] = pcs / pcns
        if pcns != 0:
          probability[i, j, k] = pcs / pcns

        print(probability[i, j, k])


# Function for reading image
def read_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to read the image at {image_path}")
        return None

    return img

# Directory containing image files
directory = "/content/drive/MyDrive/image_data/"

# Initialize the color array with zeros
global skin, nonSkin, probability, total_skin, total_non_skin
total_skin = 0
total_non_skin = 0
skin = np.zeros((256, 256, 256), dtype=np.uint32)
nonSkin = np.zeros((256, 256, 256), dtype=np.uint32)
probability = np.zeros((256, 256, 256), dtype=np.float64)

# Iterate over files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        image_path = os.path.join(directory, filename)
        mask_path = os.path.join("/content/drive/MyDrive/mask_data/",f"{filename[:-4]}.bmp")
        img_data = read_image(image_path)
        mask_data = read_image(mask_path)

        # Check if the image was successfully loaded
        if img_data is not None:
            print(f"Image {filename} loaded successfully")

        if mask_data is not None:
            print(f"Mask for {filename} loaded successfully")

        countSkinNonSkinPixels(img_data, mask_data)
        break


calcProbability()
print(img_data.shape[0]*img_data.shape[1])
