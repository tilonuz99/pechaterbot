from PIL import Image, ImageDraw, ImageFont
def rangla(mes,matn,styl,rang,size,position):
	chat_id = mes.from_user.id
	im = Image.open(str(mes.from_user.id)+".jpg")
	Width,Height = im.size
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(styl, size)
	text_w, text_h = draw.textsize(str(matn),font=font)
	if position == "tepa_chap":
		x = 0
		y = 5
	elif position == "tepa":
		x = (Width-text_w)/2
		y = 5
	elif position == "tepa,_ong":
		x = Width-text_w-5
		y = 5
	elif position == "orta_chap":
		x = 0
		y = (Height-text_h)/2
	elif position == "orta":
		x = (Width-text_w)/2
		y = (Height-text_h)/2
	elif position == "orta_ong":
		x = (Width-text_w)
		y = (Height-text_h)/2
	elif position == "past_chap":
		x = Width-text_w-5
		y = Height-text_h-5
	elif position == "past":
		x = (Width-text_w)/2-5
		y = Height-text_h-5
	elif position == "past_ong":
		x = Width-text_w-5
		y = Height-text_h-10-5
	draw.text((x,y), str(matn), fill=rang,font=font)
	ok = im.save(str(chat_id)+'water.jpg', "JPEG")
	if ok:
		return "true"