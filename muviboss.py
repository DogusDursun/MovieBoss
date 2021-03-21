import discord
import requests
import json
from replit import db

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

client.run('ODE2MDExMjI4MDE4OTAxMDUy.YD0vrQ.VTSF1ZwbJU6A5Rh5vFQ0_HXDvtI')