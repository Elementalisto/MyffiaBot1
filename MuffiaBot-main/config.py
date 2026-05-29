from utils.enums import PlayerRole


chats = {}

# players
MAX_PLAYERS = 25
MIN_PLAYERS = 7
MIN_PLAYERS_FOR_2_MAFIOSO = 12
MIN_PLAYERS_FOR_3_MAFIOSO = 18


# delays(in seconds)
registration_duration = 60
night_voting_duration = 60
conversation_duration = 60
day_voting_duration = 20

# bot messages
greetings = {PlayerRole.MAFIOSO : f'Ви *{PlayerRole.MAFIOSO}*\.\n'\
                                   'Ваша головна мета — знищити невинних\.\n'\
                                   "Удачі вам і не дозволяйте іншим гравцям здогадатися, хто ви\!",
            PlayerRole.INNOCENT:  f'Ви *{PlayerRole.INNOCENT}*\.\n'\
                                   "Мало що можна зробити, щоб зупинити мафію\,\n"\
                                   'але якщо ви співпрацюватимете з іншими невинними, ваше місто може мати шанс\.',
            PlayerRole.DETECTIVE: f'Ви *{PlayerRole.DETECTIVE}*\,\n'\
                                   "єдина надія цього міста в боротьбі з мафією\.\n"\
                                   'Удачі\!',
            PlayerRole.DOCTOR:    f'Ви *{PlayerRole.DOCTOR}*\,\n'\
                                   'Ви можете лікувати гравців, убитих вночі\.\n'\
                                   "Остерігайтеся допомоги мафії та не будьте надто егоїстичними\!"}

help_message = 'Привіт, я *MuffiaBot*\n'\
               'Я розумію ці команди:\n'\
               '• /help \- відобразити це довідкове повідомлення\n'\
               '• /start \- почати реєстрацію\n'\
               '• /begin \- завершити реєстрацію та розпочати гру\n'\
               '• /stop \- зупинити гру'\


# starting the game
game_start_message = 'Початок нової гри\!'
game_in_progress_message = 'Гра вже триває'
game_private_message = "Ти ж не можеш грати сам, чи не так?"
no_active_registration_message = 'У цьому чаті немає активної реєстрації'

# stopping the game
game_idle_message = 'Гра не працює, нічого не зупиняє'
game_stopped_message = 'Зупинити гру'
not_enough_players_message = 'Недостатньо гравців, гра не розпочнеться'

# registration
successfull_registration_message = 'Ви успішно зареєструвалися!'
early_registration_message = 'Не вдається зареєструватися, спочатку почніть гру'
late_registration_message = 'Занадто пізно, зачекайте, поки зупиниться поточна гра'
double_registration_message = 'Ви вже зареєстровані'
registration_error_message = 'Сталася помилка, спробуйте ще раз'

# during the game
game_begins_message = 'Гра починається!'
conversation_message = f'Тепер у вас є *{conversation_duration} Секунд* щоб обговорити ситуацію'
day_vote_message = f"Час лінчувати мафію, у тебе є *{day_voting_duration} Секунд* щоб зробити свій вибір"
voting_time_expired_message = 'Час голосування минув'
