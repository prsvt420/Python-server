import logging

from jinja2 import Environment, FileSystemLoader

HOST = '127.0.0.1'
PORT = 8080

logging.basicConfig(level=logging.INFO)

env_templates = Environment(loader=FileSystemLoader('templates'))

DATABASE_URL = 'sqlite:///db.sqlite3'
