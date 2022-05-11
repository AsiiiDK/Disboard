import discord
from util import uToken
from util import saving

from os import path
from os import system

def clear():
  system("clear")

# -- Start -- #
client = discord.Client()

global token

token = ''

saving.makeCommand('bob','jens')

if path.exists('token.txt') == False:
  t = input("Type your token in here:\n> ")
  uToken.setToken(t)
  token = t
else:
  token = uToken.getToken()

@client.event
async def on_ready():
  print("User logged in as: {0.user}".format(client))
  start()

def commands():
  print("[1] Add Command\n[2] Edit command")
  choice = input("> ")
  
  if choice == "1":
    cmd_name = input("Command Name: ")
    cmd_embed = bool(input("Embed command (True/False): "))
    cmd_send = input("What is the command going to send: ")

    if cmd_embed == True:
      cmd_embed_color = input("embed color (Blue, Green, Red): ")
      

def start():
  print("[1] Commands")
  print("[2] Welcome Message")
  print("[3] Reaction Roles")
  print("[4] Send message with bot")

  choice = input("> ")

  if choice =="1":
    commands()
  elif choice =="2":
    welcome()
  elif choice =="3":
    reaction()

client.run(token)