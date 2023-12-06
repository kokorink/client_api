# /client_api/main.py

from pyrogram import Client

api_id = 21154615
api_hash = 'fcd8bc096c20735fda5011f35d4befbe'

# Создаём программный клиент, передаём в него
# имя сессии и данные для аутентификации в Client API
app = Client('my_account', api_id, api_hash)

app.start()
# Отправляем сообщение
# Первый параметр - это id чата или имя получателя.
# Зарезервированное слово 'me' означает собственный аккаунт отправителя.
app.send_message('taratanta', 'Привет, это я!')
app.stop()
