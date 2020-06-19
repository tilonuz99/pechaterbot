import os
import telebot
from telebot import  types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw, ImageFont
from position import  *
from style import *
from ranglar import *
from fontsize import *
API_TOKEN = '1106274039:AAGMGgROr8O4Wr0BeIBx1qO55p79QaG92L8'
bot = telebot.TeleBot(API_TOKEN)
class User:
    def __init__(self, matn):
        self.matn = matn
def getfayl(call,ok):
	tsoz = open(str(call.message.chat.id)+ok+'.txt','r')
	soz = str(tsoz.read())
	return soz
def textsize(hajmi):
	markup = InlineKeyboardMarkup()
	markup.row_width = 3
	markup.add(InlineKeyboardButton("➖"+str(hajmi),callback_data="minus"+str(hajmi)),InlineKeyboardButton("➕"+str(hajmi),callback_data="plus"+str(hajmi)))
	markup.add(InlineKeyboardButton("↩️Qaytish.",callback_data="home"))
	
	return markup
def colours():
	markup = InlineKeyboardMarkup()
	markup.row_width = 3
	markup.add(InlineKeyboardButton("⚪️",callback_data="rangwhite"),InlineKeyboardButton("⚫️",callback_data="rangblack"))
	markup.add(InlineKeyboardButton("↩️Qaytish.",callback_data="home"))
	return markup
def stil():
    markup = InlineKeyboardMarkup()
    markup.row_width = 5
    btn_list = []
    for i in range(1,41):
        btn_list.append(InlineKeyboardButton(i,callback_data="stile"+str(i)))
    btn_list = list(split_list(btn_list, 5))
    for b in btn_list:
        markup.add(*b)
    markup.add(InlineKeyboardButton("↩️Qaytish.",callback_data="home"))
    return markup
def split_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
def rasm():
	markup = InlineKeyboardMarkup()
	markup.row_width = 2
	markup.add(InlineKeyboardButton("💠Matn ko'rinishi",callback_data="style"),InlineKeyboardButton("📐Matn o'lchami",callback_data="size"),InlineKeyboardButton("🎨Matn rangi",callback_data="color"),InlineKeyboardButton("📍Matn joylashuvi",callback_data="position"))
	return markup
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("↖️", callback_data="tepa_chap"),InlineKeyboardButton("⬆️", callback_data="tepa"),InlineKeyboardButton("↗️",callback_data="tepa_ong"))
    
    markup.add(InlineKeyboardButton("⬅️", callback_data="orta_chap"),InlineKeyboardButton("⏺", callback_data="orta"),InlineKeyboardButton("➡️",callback_data="orta_ong"))
    markup.add(InlineKeyboardButton("↙️️", callback_data="past_chap"),InlineKeyboardButton("⬇️", callback_data="past"),InlineKeyboardButton("↘️️",callback_data="past_ong"))
    markup.add(InlineKeyboardButton("↩️Qaytish.",callback_data="home"))
    return markup
user_dict = {}
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """Salom botga xush kelibsiz.Ushbu bot orqali o'z rasmlaringizga ismingizni yozishingiz mumkin.Shunchaki rasmingizni yuboring.""")
    bot.register_next_step_handler(msg, getphoto)

def getphoto(mes):
	if mes.photo:
		chat_id = str(mes.from_user.id)
		fileID = mes.photo[-1].file_id
		file = bot.get_file(fileID)
		path=file.file_path
		download = bot.download_file(path)
		with open(str(mes.from_user.id)+".jpg",'wb') as newfile:
			newfile.write(download)
		bot.reply_to(mes,"🖼Rasmingiz qabul qilindi.\nEndi ismingizni yuboring.")
		joyi = "position.txt"
		fayl = chat_id + joyi
		with open(fayl,'w') as yoz:
			yoz.write("orta")
		matnturi = "font.txt"
		yozish = chat_id + matnturi
		with open(yozish,'w') as yoz:
			yoz.write(" 1.ttf")
		matnrangi = "color.txt"
		yozish = chat_id + matnrangi
		with open(yozish,'w') as yoz:
			yoz.write("white")
		matnxajmi = "size.txt"
		yozish = chat_id + matnxajmi
		with open(yozish,'w') as yoz:
			yoz.write("100")
			
		bot.register_next_step_handler(mes, added)
	else:
		msg=bot.reply_to(mes,"Bunday buyruq mavjud emas.")
		bot.register_next_step_handler(msg, getphoto)
		
def added(mes):
	if mes.text:
		chat_id = str(mes.from_user.id)
		formati = ".txt"
		yozish = chat_id + formati
		text = mes.text
		ok = User(mes.text)
		user_dict[chat_id] = ok
		user = user_dict[chat_id]
		matn = user.matn
		with open(yozish,'w') as yoz:
			yoz.write(mes.text)
		
		im = Image.open(str(mes.from_user.id)+".jpg")
		Width,Height = im.size
		draw = ImageDraw.Draw(im)
		font = ImageFont.truetype(" 1.ttf", 100)
		text_w, text_h = draw.textsize(str(matn),font=font)
		x = (Width-text_w)/2
		y = (Height-text_h)/2
		draw.text((x,y-10), str(matn), fill="white",font=font)
		im.save(chat_id+"water.jpg", "JPEG")
		bot.send_photo(mes.from_user.id,open(chat_id+"water.jpg",'rb'),reply_markup=rasm())
	else:
		msg=bot.reply_to(mes,"Bunday buyruq mavjud emas.")
		bot.register_next_step_handler(msg, added)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
	chat_id = str(call.message.chat.id)
	if os.path.exists(str(call.message.chat.id)+'.txt'):
	    t = open(str(call.message.chat.id)+'.txt','r')
	else:
		bot.reply_to(call.message,"Iltimos qayta /start buyrug'ini yuboring")
	styl = open(str(call.message.chat.id)+'font.txt').read()
	ok = User(str(t.read()))
	user_dict[chat_id] = ok
	user = user_dict[chat_id]
	matn = user.matn
	pos = getfayl(call,"position")
	turi = getfayl(call,"font")
	hajmi = getfayl(call,"size")
	rangi = getfayl(call,"color")
	if call.data == "position":
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=gen_markup())
	elif call.data == "style":
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=stil())
	elif call.data == "color":
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=colours())
	elif call.data == "size":
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=textsize(int(hajmi)))
	elif "minus" in call.data:
		xajmi = call.data.replace("minus","")
		xajmi = int(xajmi) -5
		fontsize(call,pos,turi,matn,rangi,int(xajmi))
		with open(str(chat_id)+'size.txt','w') as yoz:
			yoz.write(str(xajmi))
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=textsize(int(hajmi)-5))
	elif "plus" in call.data:
		xajmi = call.data.replace("plus","")
		xajmi = int(xajmi) + 5
		fontsize(call,pos,turi,matn,rangi,int(xajmi))
		with open(str(chat_id)+'size.txt','w') as yoz:
			yoz.write(str(xajmi))
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=textsize(int(hajmi)+5))
	elif "rang" in call.data:
		rangi = call.data.replace('rang','')
		rangla(call,matn,turi,rangi,int(hajmi),pos)
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=colours())
		with open(str(chat_id)+'color.txt','w') as yoz:
			yoz.write(rangi)
	elif "stile" in call.data:
		stile = call.data.replace("stile","")
		style(call,pos," "+str(stile)+".ttf",matn,rangi,int(hajmi))
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=stil())
		
		with open(str(chat_id)+'font.txt','w') as yoz:
			yoz.write(" "+str(stile)+".ttf")
	elif call.data == "tepa_ong":
		tepa_ong(call,matn,styl,int(hajmi),rangi)
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=gen_markup())
		formati = "position.txt"
		yozish = chat_id + formati
		with open(yozish,'w') as yoz:
			yoz.write(call.data)
	elif call.data == "tepa_chap":
		tepa_chap(call,matn,styl,int(hajmi),rangi)
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=gen_markup())
		formati = "position.txt"
		yozish = chat_id + formati
		with open(yozish,'w') as yoz:
			yoz.write(call.data)
	elif call.data == "tepa":
		tepa(call,matn,styl,int(hajmi),rangi)
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=gen_markup())
		formati = "position.txt"
		yozish = chat_id + formati
		with open(yozish,'w') as yoz:
			yoz.write(call.data)
	elif call.data == "orta_chap":
		orta_chap(call,matn,styl,int(hajmi),rangi)
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=gen_markup())
		formati = "position.txt"
		yozish = chat_id + formati
		with open(yozish,'w') as yoz:
			yoz.write(call.data)
	elif call.data == "orta":
		orta(call,matn,styl,int(hajmi),rangi)
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=gen_markup())
		formati = "position.txt"
		yozish = chat_id + formati
		with open(yozish,'w') as yoz:
			yoz.write(call.data)
	elif call.data == "orta_ong":
		orta_ong(call,matn,styl,int(hajmi),rangi)
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=gen_markup())
		formati = "position.txt"
		yozish = chat_id + formati
		with open(yozish,'w') as yoz:
			yoz.write(call.data)
	elif call.data == "past_chap":
		past_chap(call,matn,styl,int(hajmi),rangi)
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=gen_markup())
		formati = "position.txt"
		yozish = chat_id + formati
		with open(yozish,'w') as yoz:
			yoz.write(call.data)
	elif call.data == "past":
		past(call,matn,styl,int(hajmi),rangi)
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=gen_markup())
		formati = "position.txt"
		yozish = chat_id + formati
		with open(yozish,'w') as yoz:
			yoz.write(call.data)
	elif call.data == "past_ong":
		past_ong(call,matn,styl,int(hajmi),rangi)
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=gen_markup())
		formati = "position.txt"
		yozish = chat_id + formati
		with open(yozish,'w') as yoz:
			yoz.write(call.data)
	elif call.data == "home":
		image = open(str(chat_id)+'water.jpg', 'rb')
		bot.edit_message_media(media=types.InputMedia(type='photo', media=image),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=rasm())
		
bot.enable_save_next_step_handlers(delay=2)
bot.polling(none_stop=True)
