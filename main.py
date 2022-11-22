from pyrogram import Client, filters

#Conectar bot con el cliente
app = Client(
"bot",
api_id="", #Ingresa tu api_id
api_hash="", #Ingresa tu api_hash
bot_token="") #Ingresa el token de tu bot
 
@app.on_message()
def commands(client, message):
    text = message.text
    username = message.from_user.username

    if '/start' in text:
        msg_start = f'🔰Bienvenido {username}'
        message.reply(msg_start)
        
print('👾Bot Online👾')
app.run()