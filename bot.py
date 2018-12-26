import discord

client = discord.Client() 
@client.event
async def on_ready():
  print("hi")

@client.event
async def on_message(message):
  a = message.content
  if message.author != client.user:
    if 'hi' in a:
       await client.send_message(message.channel, "suprise muthafuka!!")
    
client.run("NTI3NDU0OTYyODE3NDMzNjAx.DwT_Ow.lfLZdJXX8FXthJrSy_TYsAtTDEc")