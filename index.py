# index.py
from mangum import Mangum
from app import app

handler = Mangum(app)
