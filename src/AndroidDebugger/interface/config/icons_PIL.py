from PIL import Image


battery_icons_size = (20,20)

battery_None = Image.open("res\\icons\\None.png").resize((battery_icons_size))
battery_Twenty =Image.open("res\\icons\\20%.png").resize((battery_icons_size))
battery_Fifty = Image.open("res\\icons\\50%.png").resize((battery_icons_size))
battery_Eighty = Image.open("res\\icons\\80%.png").resize((battery_icons_size))
battery_One_hundred = Image.open("res\\icons\\100%.png").resize((battery_icons_size))