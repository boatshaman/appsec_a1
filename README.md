###### Application Security - Assignment 1
# Image Resizer

Basic python script to resize an image to a square. Fills in extra space with the color black. 
I've added Travis CI to the project but only have a placeholder test at the moment in [test_image_resize.py](https://github.com/boatshaman/appsec_a1/blob/master/test_image_resize.py)

#### Running the Code
To run first make sure you have the requirements installed:
`pip install -r requirements.txt`

Make sure the script is executable: `chmod +x image_resize.py`

And then find an image you would like to resize and run the script as such:
`./image_resize.py test_image.jpg`

**Note:** It should work with any type of image but I haven't actually tested it with other image types yet. This will be done in the future.

