#! /usr/bin/python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/podclass')
from main import app as application
application.secret_key = '91e500f2-f506-4175-b09a-423db38275d0'
