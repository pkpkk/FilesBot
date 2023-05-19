from pyrogram import Client,filters
from subprocess import Popen
import os
from urllib.parse import quote

FILE_PATH=os.path.join(os.getcwd(),'files/')
TOKEN=os.getenv('TOKEN')
API_ID=os.getenv('API_ID')
HASH=os.getenv('HASH')

app=Client('app',bot_token=TOKEN,api_id=API_ID,api_hash=HASH,workers=200)

@app.on_message(filters.video | filters.document | filters.audio)
async def mak_url(cl,msg):
  up=await msg.reply('downloading')
  file=await msg.download(file_name=FILE_PATH)
  await up.edit(f'link is my app domain/{file}')

@app.on_message(filters.command('/start'))
async def stsr(cl,msg):
  await msg.reply('I am up')
  
if __name__=='__main__':
  Popen(f"gunicorn web:web_app --bind 0.0.0.0:{os.getenv('PORT')}",shell=True)
  app.run()
