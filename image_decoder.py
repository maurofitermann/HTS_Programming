from PIL import Image
import re
img = Image.open("./PNG.png")

white_pixel_coordinates = []
for height in range(img.size[1]):
    for width in range(img.size[0]):
        if (img.getpixel((width, height))==1):
            white_pixel_coordinates.append((width, height))

pixel_numbers = []
for coordinate in white_pixel_coordinates:
    pixel_number = coordinate[0]+img.size[0]*coordinate[1]
    pixel_numbers.append(pixel_number)

print(pixel_numbers)

hidden_values = [pixel_numbers[0]]
for x in range(1, len(pixel_numbers)):
        hidden_values.append(pixel_numbers[x]-pixel_numbers[x-1])

print(hidden_values)

message_morse=""

for value in hidden_values:
    message_morse+=chr(value)

print(message_morse)

split_morse = re.split('[/ ]', message_morse)
print(split_morse)

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def decode(dots_and_slashes_and_dashes):
    message_plaintext = ''
    for value in dots_and_slashes_and_dashes:
        for character, morse in morse_dict.items():
            
            if morse == value:
            
                message_plaintext += character
    
    
    
    return message_plaintext
message_plaintext = decode(split_morse)
print(message_plaintext)