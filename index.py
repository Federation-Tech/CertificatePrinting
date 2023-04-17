from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("cert.png")

file1 = open("file.txt", "r")

list1 = file1.readlines()

x = 1

for participant in list1:
    my_image = Image.open("cert.png")
    font = ImageFont.truetype("CenturyGothic.ttf", 180)
    text = list1[x - 1].split("\t")[0]
    font_width = font.getsize(text)[0]
    font_height = font.getsize(text)[1]

    print(participant)
    editable_image = ImageDraw.Draw(my_image)

    editable_image.text(
        (3250, 3250), text.center(0), font=font, fill=(0, 0, 0)
    )

    font2 = ImageFont.truetype("CenturyGothic.ttf", 100)
    font_width = font2.getsize(text)[0]
    font_height = font2.getsize(text)[1]

    slNo = str(x)

    editable_image.text(
        (7400, 1100), slNo.center(0), font=font2, fill=(0, 0, 0)
    )

    my_image.save((participant[0:-2]+".png").format(x))
    x = x + 1
