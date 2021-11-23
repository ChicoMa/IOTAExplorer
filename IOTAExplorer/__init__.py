from flask import Flask 

IOTAExplorer = Flask(__name__)

from IOTAExplorer import views
from IOTAExplorer import admin_views