import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor



vk_session = vk_api.VkApi(token='08e793f049b07c7c8ea5eb92d4a995eb29cf4e697a5b4093cc4f626f60ba3c8cf73318f42c6d560b58220') #токен вашей группы
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session,213255912) #цифровой id вашей группы
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
	
	keyboard1.add_button('Собачим vto.pe', color=VkKeyboardColor.POSITIVE)
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
						vk.messages.send(peer_id=event.object.peer_id, message="@all Беседа хуйня ливаем Слушай лох, на хуй соси и не скули пока я твою мать не начал ебать =D ОРГАНИЗАТОР vk.com/bld71 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐󠁧󠁢󠁷󠁬🏴 󠁧󠁢󠁷󠁬󠁳󠁿",keyboard=keyboard1.get_keyboard(), random_id=0)	
					
			
		except Exception as e:
			print('') 

if __name__ == '__main__':
	main()