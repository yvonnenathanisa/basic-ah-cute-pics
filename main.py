from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open('original.jpg') as pic_original:
    print('Image is open\nSize:', pic_original.size)
    print('Format:', pic_original.format)
    print('Type:', pic_original.mode)
    pic_original.show()

    pic_monochrome = pic_original.convert("L")
    pic_monochrome.save("desaturated_picture.jpg")
    print('Image is open\nSize:', pic_monochrome.size)
    print('Format:', pic_monochrome.format)
    print('Type:', pic_monochrome.mode)
    pic_monochrome.show()

    pic_blur = pic_original.filter(ImageFilter.BLUR)
    pic_blur.save('unseeable_picture.jpg')
    print('Image is open\nSize:', pic_blur.size)
    print('Format:', pic_blur. format)
    print('Type:', pic_blur.mode)
    pic_blur.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save("up_picture.jpg")
    pic_up.show()

    pic_mirror = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirror.save('mirror_picture.jpg')
    pic_mirror.show()

    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save('contr.jpg')
    pic_contrast.show()