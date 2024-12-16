import sys
import os

import django

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

django.setup()
