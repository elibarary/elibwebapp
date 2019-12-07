"""
WSGI config for library project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')

#application = get_wsgi_application()
activate_this = 'C:/Users/elibrary/Documents/Electronic_library/libraryenv/libenv/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# add python site packages, you can use virtualenvs also
site.addsitedir("C:/Users/elibrary/Documents/Electronic_library/libraryenv/libenv/Lib/site-packages")

# Add the app's directory to the PYTHONPATH 
sys.path.append('C:/Users/elibrary/Documents/Electronic_library/librarysrc/library') 
sys.path.append('C:/Users\elibrary/Documents/Electronic_library/librarysrc/library/library')  

os.environ['DJANGO_SETTINGS_MODULE'] = 'library.settings' 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")  
 
application = get_wsgi_application()
