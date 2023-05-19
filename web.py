from flask import send_from_directory,Flask
import os
from app import FILE_PATH

PORT=os.getenv('PORT')
HOST=os.getenv('HOST') if os.getenv('HOST') else 'https://0.0.0.0'
os.mkdir(FILE_PATH)
web_app=Flask(__name__)

@web_app.route('/')
def list_f():
  html=""
  for file in os.listdir(FILE_PATH):
    html+=f'<a href="{HOST}/{file}"> {file} </a>'
  return '<p>'+html+'</p>'

@web_app.route('/<name>')
def sendf(name):
  return send_from_directory(FILE_PATH,name)


if __name__=='__main__':
  web_app.run()
