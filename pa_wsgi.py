from werkzeug.debug import DebuggedApplication
from application import create_app
import os
import sys
from dotenv import load_dotenv

python_anywhere_username = 'jorge3'
path = '/home/' + python_anywhere_username + '/opt/flogger'
if path not in sys.path:
    sys.path.append(path)

load_dotenv(os.path.join(path, '.flaskenv'))

app = create_app()

application = DebuggedApplication(app, evalex=True)
