from flask import Flask

app = Flask('spi4ka_API')

from . import routes
