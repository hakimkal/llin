PRODUCTION = False
DBNAME = 'llin'
PRODUCTION_STATIC_ROOT = '/home/lep12/webapps/staticprimegate/'
PRODUCTION_STATIC_URL = 'http://primegateacademy.com/staticprimegate/'
if PRODUCTION == True:
    DBUSER = 'primegate'                     # Not used with sqlite3.
    DBPASS = 'hotoro'
    
else:
    DBUSER = 'postgres'                     # Not used with sqlite3.
    DBPASS = 'hotoro'

#EMAIL SMTP
EMAIL_HOST = "smtp.webfaction.com"
EMAIL_PORT = 587
EMAIL_HOST_USER =  "primegate"
EMAIL_HOST_PASSWORD = "primegate1nfo"
EMAIL_USE_TLS = True
