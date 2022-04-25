from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def watermark_image(img_path, output_path, text, position):
    img = Image.open(img_path)
    drawing = ImageDraw.Draw(img)
    black = (10, 5, 12)
    drawing.text(position, text, fill=black)
    img.show()
    img.save(output_path)


img = 'test.jpg'
watermark_image(img, 'watermarked.jpg', 'Python', position(0, 0))
