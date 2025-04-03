"""
Production settings
"""
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']

# Add more secure settings for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
