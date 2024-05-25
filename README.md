# Steganography
Created as a school project

### How it works?
First and foremost, you need to know that this program only works with Portable Pixmap (PPM) ASCII files.

The program begins by reading all the pixels of the image contained in the PPM file. It then encodes the message, including a signature to facilitate decryption, using the pixels. The message is converted into binary, and each pixel is adjusted to be even or odd: even represents 0, and odd represents 1.

### Why doesn't it support other types of Portable Pixmap?
This project only works with P3 Portable Pixmap (and earlier versions) because P4 Portable Pixmap (and later versions) are encoded in a combination of binary and text, making it more challenging to properly read the file.

### Why can't I use normal images directly in the program?
The reason is that I haven't found any library or resource that allows this functionality. It is possible for P4 Portable Pixmap and later versions, but not for P3 and earlier versions.

### Note:
I've added the files that I have used to test my program. Hope it helps you to test my project.

#
Thanks for reading!
Want to go further? [Click here](https://www.geeksforgeeks.org/image-based-steganography-using-python/). This can help you if you want to work directly on images.
