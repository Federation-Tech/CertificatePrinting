from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("cert.jpeg")

file1 = open("file.txt", "r")

list1 = file1.readlines()

x = 1

for participant in list1:
    my_image = Image.open("cert.jpeg")
    width = my_image.width
    height = my_image.height
    font = ImageFont.truetype("Roboto-Medium.ttf", 48)
    text = list1[x - 1].split("\t")[0]
    font_width = font.getsize(text)[0]
    font_height = font.getsize(text)[1]

    print(participant)
    start_x = (width / 2 - 30 - font_width) / 2
    editable_image = ImageDraw.Draw(my_image)

    editable_image.text(
        (width / 2 - 75 + start_x, height / 2 + 25), text, (218, 165, 32), font=font
    )

    my_image.save(("result{}.jpeg").format(x))
    x = x + 1
