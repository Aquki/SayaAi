# SayaAi
This is a discord bot with a c.ai characters integration by an unofficial library made from kramcat, check their GitHub for more information about how the library works [here](https://github.com/kramcat/CharacterAI)

# Requirements
first, clone the repository (you need git to clone it)
```bash
git clone https://github.com/Aquki/SayaAi.git
```
then cd into it
```bash
cd SayaAi
```
and install the requirements.txt
```bash
pip install -r requirements.txt
```
and you need also to install the c.ai library with this command
```bash
pip install git+https://github.com/kramcat/CharacterAI.git
```
and you are ready!

# Setup
edit the .env file with your tokens and message

In the beginning, you have the first message value, if the chat ID is None, this message will sent first to the c.ai character
``` 
first_message=Hello! You are inside discord bot
```
then you have the c.ai token, there are a lot of ways to get it but kramcat made their own way [here](https://docs.kram.cat/auth.html)
```
char_token= 
```
and the character ID, you can find it on the link of the character you want
![image](https://github.com/user-attachments/assets/18a751c7-6e7f-4bb4-b403-ddb50e26774a)
```
char_id=zzOyOQAL5HuNBiUZXgNOrRYjEqT2YHRP6jWDkzoVVzY
```
you can set this value to None and the bot will create a new chat every time you run it, and you can make it remember the chat by set the chatID, When you run the bot with None ChatID it will create one for you and then you can copy it and set it as the chat_id value and it will continue the chat every time you run it again
![image](https://github.com/user-attachments/assets/3e2ef2ea-7d58-4809-995c-004eeb025ca9)
```
chat_id=None
```
here set the discord token of your bot, you can get it from the discord developer portal [here](https://discord.com/developers)
```
token=
```
# Run
after you end from set your tokens, you can run the bot by
```bash
python3 SayaAi.py
```

# Thanks
Thank you Toranya!
