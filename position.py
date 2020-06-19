from PIL import Image, ImageDraw, ImageFont
def tepa_chap(mes,matn,styl,size,color):
	chat_id = mes.from_user.id
	im = Image.open(str(mes.from_user.id)+".jpg")
	Width,Height = im.size
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(styl, size)
	text_w, text_h = draw.textsize(str(matn),font=font)
	x = (Width-text_w)/2
	y = (Height-text_h)/2
	draw.text((0,5), str(matn), fill=color,font=font)
	ok = im.save(str(chat_id)+'water.jpg', "JPEG")
	if ok:
		return "true"
def tepa(mes,matn,styl,size,color):
	chat_id = mes.from_user.id
	im = Image.open(str(mes.from_user.id)+".jpg")
	Width,Height = im.size
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(styl, size)
	text_w, text_h = draw.textsize(str(matn),font=font)
	x = (Width-text_w)/2
	y = (Height-text_h)/2
	draw.text((x,5), str(matn), fill=color,font=font)
	ok = im.save(str(chat_id)+'water.jpg', "JPEG")
	if ok:
		return "true"
		
def tepa_ong(mes,matn,styl,size,color):
	chat_id = mes.from_user.id
	im = Image.open(str(mes.from_user.id)+".jpg")
	Width,Height = im.size
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(styl, size)
	text_w, text_h = draw.textsize(str(matn),font=font)
	x = Width-text_w-5
	y = (Height-text_h)/2
	draw.text((x,10), str(matn), fill=color,font=font)
	ok = im.save(str(chat_id)+'water.jpg', "JPEG")
	if ok:
		return "true"

def orta_ong(mes,matn,styl,size,color):
	chat_id = mes.from_user.id
	im = Image.open(str(mes.from_user.id)+".jpg")
	Width,Height = im.size
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(styl, size)
	text_w, text_h = draw.textsize(str(matn),font=font)
	x = (Width-text_w)
	y = (Height-text_h)/2
	draw.text((x,y), str(matn), fill=color,font=font)
	ok = im.save(str(chat_id)+'water.jpg', "JPEG")
	if ok:
		return "true"
		
def orta(mes,matn,styl,size,color):
	chat_id = mes.from_user.id
	im = Image.open(str(mes.from_user.id)+".jpg")
	Width,Height = im.size
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(styl, size)
	text_w, text_h = draw.textsize(str(matn),font=font)
	x = (Width-text_w)/2
	y = (Height-text_h)/2
	draw.text((x,y), str(matn), fill=color,font=font)
	ok = im.save(str(chat_id)+'water.jpg', "JPEG")
	if ok:
		return "true"
		
def orta_chap(mes,matn,styl,size,color):
	chat_id = mes.from_user.id
	im = Image.open(str(mes.from_user.id)+".jpg")
	Width,Height = im.size
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(styl, size)
	text_w, text_h = draw.textsize(str(matn),font=font)
	x = (Width-text_w)
	y = (Height-text_h)/2
	draw.text((0,y), str(matn), fill=color,font=font)
	ok = im.save(str(chat_id)+'water.jpg', "JPEG")
	if ok:
		return "true"
		
		
def past_ong(mes,matn,styl,size,color):
	chat_id = mes.from_user.id
	im = Image.open(str(mes.from_user.id)+".jpg")
	Width,Height = im.size
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(styl, size)
	text_w, text_h = draw.textsize(str(matn),font=font)
	x = Width-text_w
	y = Height-text_h-10
	draw.text((x,y), str(matn), fill=color,font=font)
	ok = im.save(str(chat_id)+'water.jpg', "JPEG")
	if ok:
		return "true"
		
def past(mes,matn,styl,size,color):
	chat_id = mes.from_user.id
	im = Image.open(str(mes.from_user.id)+".jpg")
	Width,Height = im.size
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(styl, size)
	text_w, text_h = draw.textsize(str(matn),font=font)
	x = (Width-text_w)/2
	y = Height-text_h
	draw.text((x-5,y-10), str(matn), fill=color,font=font)
	ok = im.save(str(chat_id)+'water.jpg', "JPEG")
	if ok:
		return "true"
		
def past_chap(mes,matn,styl,size,color):
	chat_id = mes.from_user.id
	im = Image.open(str(mes.from_user.id)+".jpg")
	Width,Height = im.size
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(styl, size)
	text_w, text_h = draw.textsize(str(matn),font=font)
	x = Width-text_w
	y = Height-text_h
	draw.text((5,y-10), str(matn), fill=color,font=font)
	ok = im.save(str(chat_id)+'water.jpg', "JPEG")
	if ok:
		return "true"