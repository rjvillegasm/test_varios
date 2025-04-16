from PIL import Image

# Caracteres ASCII ordenados por intensidad
ASCII_CHARS = ['@', '#', '8', '&', 'o', ':', '*', '.', ' ']

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = float(height) / float(width)
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def image_to_ascii(image, new_width=100):
    image = resize_image(image)
    grayscale_image = image.convert('L')  # Convertir a escala de grises
    pixels = list(grayscale_image.getdata())  # Obtener los píxeles en una lista
    ascii_str = ''
    try:
        for pixel_value in pixels:
            ascii_str += ASCII_CHARS[pixel_value // 32]  # Ajustar el divisor según los valores de gris esperados
            if len(ascii_str) % new_width == 0:
                ascii_str += '\n'
    except IndexError:
        pass  # Manejar el caso donde pixel_value // 32 puede estar fuera del rango de ASCII_CHARS
    return ascii_str

def main(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    
    ascii_str = image_to_ascii(image)
    print(ascii_str)

if __name__ == '__main__':
    image_path = r'C:\misrepositorios\test_varios\ACSII_art\imagenes\222.png'
    main(image_path)
