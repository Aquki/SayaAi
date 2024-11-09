import discord
from discord.ext import commands
from characterai import aiocai
from termcolor import colored
from os import getenv
from dotenv import load_dotenv

# Discord bot setup
response = False
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)


#load env values
load_dotenv()
char_id = getenv("char_id")
chat_id = getenv("chat_id")
char_token = getenv("char_token")
first_message = getenv("first_message")
token = getenv("token")

client = aiocai.Client(char_token)


async def loga(char_id, id=None):
    char_info = await client.get_char(char_id)
    print(colored("Created Character.ai session:", 'green', attrs=['bold']))
    print(colored("C.Ai Status: OK!", 'green'))
    print(colored("Character: ", 'magenta'), char_info.name)
    print(colored("ChatID: ", 'magenta'), id)
    print(colored("CharacterID: ", 'magenta'), char_info.external_id)

# fetch the current user in c.ai
async def get_character_user():
    try:
        return await client.get_me()
    
    except AttributeError as e:
        print(f"An error occurred: {e}")
        return None


#the chat function
async def start_chat(text):
    global chat_id
    me = await get_character_user()
    
    # If there is no chat session, start a new one
    if chat_id is None:
        async with await client.connect() as chat:
            new, answer = await chat.new_chat(char_id, me.id)
            chat_id = new.chat_id 
            message = await chat.send_message(char_id, chat_id, text)

            return message
    else:
        # If chat already exists, send the message in the existing chat
        async with await client.connect() as chat:
            message = await chat.send_message(char_id, chat_id, text)
            return message


# Event when bot is ready
@bot.event
async def on_ready():
    global first_message
    print(colored(f'Bot: {bot.user}!', 'cyan', attrs=['bold']))

    if chat_id is None:
        # Automatically send a first message to CharacterAI when the bot starts
        await start_chat(first_message)
        await loga(char_id, id=chat_id)
    else:
        await loga(char_id, id=chat_id)
    

# Event when bot is mentioned
@bot.event
async def on_message(message):
    global response
    if bot.user.mentioned_in(message):
            
        
        async with message.channel.typing():
            if response == True:
                return
            response = True
            user_message = message.content.replace(f'<@{bot.user.id}>', '').strip()

            if user_message:
                # Format the message as "Username: message"
                formatted_message = f"{message.author.display_name}: {user_message}"
                
                # Send the formatted message to CharacterAI
                char_response = await start_chat(formatted_message)
                # Reply to the user who mentioned the bot
                await message.reply(f'{char_response.text}')
                response = False


                with open("log.txt", "a", encoding="utf-8") as fr:
                    fr.write(f"{str(formatted_message)} / {str(char_response.name)}: {str(char_response.text)}\n")
            else:
                await message.reply("You need to send me a message to forward to CharacterAI! BAKA YARO")
    await bot.process_commands(message)

# Run the bot with the Discord bot token
bot.run(token, log_handler=None)
