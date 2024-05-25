import os

def getPixels(fileName):
    """This function is used to get all the pixels, width, height, max value from image

    Args:
        fileName (string): File name [Without extension]

    Returns:
        pixels (list): Returns a list of pixels colors
        width (int): Returns image width
        height (int): Returns image height
        max_value (int): Returns max value
    """
    pixels = []
    
    with open(fileName, 'r') as f:
        # Skip P3 line
        f.readline().strip()
        
        # Get Width and Height to get all the pixels
        width, height = map(int, f.readline().split())
        
        # Get the max value
        max_value = f.readline().strip()
        
        # Read pixel data
        for h in range(height):
            for w in range(width):
                for pixel in f.readline().split():
                    pixels.append(pixel)
    return pixels, width, height, max_value

def encode(fileName, message):    
    # Initialization
    message_chars = []
    
    assert os.path.isfile(fileName), "Image not found!"
    assert message != "", "Message cannot be empty."
    
    message += "<s_i_g_n_a_t_u_r_e_do_not_touch_this>"
    
    # Converts all the characters in the message to binary
    for message_char in message:
        message_chars.append(format(ord(message_char), '08b'))
    
    
    # Get all the informations required from the image
    pixels, width, height, max_value = getPixels(fileName)
        
    assert(len(message) < width * height), "Message cannot be longer than the size of the image."
        
    index = 0
        
    """
        We will be looping through messages characters to hide every character in a color (R, G, B). We will be checking if we need to hide a 0 or a 1. If it's a 0 we will make the color
        number even otherwise if we need a 1 we will make the color odd.
    """
    for binary in message_chars:
        for bit in binary:
            if (bit == '0' and int(pixels[index]) % 2 != 0 and int(pixels[index]) != 255) or (bit == '1' and int(pixels[index]) % 2 == 0 and int(pixels[index])):
                pixels[index] = (int(pixels[index]) + 1)
                index += 1
            elif (bit == '0' and int(pixels[index]) % 2 == 0) or (bit == '1' and int(pixels[index]) % 2 != 0 and int(pixels[index]) != 255):
                pixels[index] = (int(pixels[index]))
                index += 1
            elif bit == '0' and int(pixels[index]) == 255:
                pixels[index] = (int(pixels[index]) - 1)
                index += 1
   
    index = 0
        
    # Save the encoded file
    with open(fileName.split('.')[0] + '-encrypted.' + fileName.split('.')[1], 'w') as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write(max_value + "\n")
            
        for pixel in pixels:
            if index % 3 == 0:
                f.write("\n")
                index = 0
            f.write(str(pixel) + " ")
            index += 1
            
    return "File has been succesfully encoded."

def decode(fileName):
    letters = []
    message = ""
    
    assert os.path.isfile(fileName), "Image not found!"
    
    # Get all the informations required from the image
    pixels, width, height, max_value = getPixels(fileName)
        
    # Initialized at -1 since we do +1 when starting to loop
    wordIndex = -1
    for i in range(len(pixels)):
        # Give us bytes instead of bits so we can easily convert to a character
        if i % 8 == 0:
            letters.append("")
            wordIndex += 1
            
        if int(pixels[i]) % 2 == 0:
            letters[wordIndex] += "0"
        elif int(pixels[i]) % 2 != 0:
            letters[wordIndex] += "1"
    
    for letter in letters:
        if "<s_i_g_n_a_t_u_r_e_do_not_touch_this>" in message:
            message = message.replace('<s_i_g_n_a_t_u_r_e_do_not_touch_this>', '')
            break
        
        # Check if the letter ascii is a character
        if int(letter, 2) > 31 and int(letter, 2) < 127:
            message += chr(int(letter, 2))
    
    print('[>>] Message =>', message)
    return "File has been succesfully decoded."
    

def main():
    """
        Main menu
    """
    
    os.system('cls')
    print('Welcome to Steganography => github.com/D1og0')
    print()
    print('[1] Encode') 
    print('[2] Decode') 
    print()
    userInput = int(input('[>>] '))
    print()
    
    if userInput != 1 and userInput != 2:
        main()
    
    print('[>>] Enter image path [With extension]')
    imagePath = input('[>>] ')
    print()
    
    if userInput == 1:
        print('[>>] Enter your message')
        message = input('[>>] ')

        
        print(encode(imagePath, message))
    elif userInput == 2:
        print(decode(imagePath))
main()