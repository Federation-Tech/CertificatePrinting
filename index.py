from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("cert.png")

file1 = open("file.txt", "r")

list1 = file1.readlines()

x = 1

for participant in list1:
    my_image = Image.open("cert.png")
    width = my_image.width
    height = my_image.height
    font = ImageFont.truetype("Rubik-Regular.ttf", 250)
    text = list1[x - 1].split("\t")[0]
    font_width = font.getsize(text)[0]
    font_height = font.getsize(text)[1]

    print(participant)
    start_x = (width / 2 - 30 - font_width) / 2
    editable_image = ImageDraw.Draw(my_image)

    editable_image.text(
        (1450, 2359), text.center(55), font=font,fill=(0, 0, 0)
    )

    my_image.save((participant[0:-2]+".png").format(x))
    x = x + 1
