# -*- coding: utf-8 -*-
"""
Django settings for EMadmin project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from django.core.urlresolvers import reverse_lazy
from os.path import dirname, join, exists
import os

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__)))
STATICFILES_DIRS = [join(BASE_DIR, 'static')]
MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'django_settings_export.settings_export',
            ],
        },
    },
]

# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
##SECRET_KEY = env('SECRET_KEY')
SECRET_KEY='i1u*m_g^bqs7o0+dh*-6s+-xfbi+t)&&x26xv+imt52zo)6v90'


ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'invoice',

    'authtools',
    'crispy_forms',
    'easy_thumbnails',

    'profiles',
    'accounts',

    'create_proj',
    'create_report',
    'django_tables2',
    'create_stat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'EMadmin.urls'

WSGI_APPLICATION = 'EMadmin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    #'default': env.db(),
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
#DATABASE_URL='sqlite:///db.sqlite3'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'WET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

ALLOWED_HOSTS = []

# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")

THUMBNAIL_EXTENSION = 'png'     # Or any extn for your thumbnails

import socket, os
hostName =  socket.gethostname()
import getpass
user = getpass.getuser()
if hostName == 'linux-bxmv.suse':
    BACKUPPATH='/run'
else:
    BACKUPPATH="/"
BACKUPPATH=os.path.join(BACKUPPATH,"media", user)
DEFAULTWORKFLOW="BASIC_Import_Mcorr2_Ctffind4_Summary"
DEFAULTWORKFLOWID=2
if user == "scipionuser":
    SCIPIONPATH = os.getenv('SCIPION_PATH','/usr/local/scipion')
    SCIPIONUSERDATA='/home/scipionuser/ScipionUserData'
else:
    SCIPIONPATH='/home/roberto/Scipion/scipion_facilities'
    SCIPIONUSERDATA='/home/roberto/ScipionUserData'
NUMBERCONCEPTS=21

DEFAULTMIC=1
#DEFAULTWORKFLOW=2
WORKFLOWFILENAME='workflow.json'
EMAILFROM="noreply-scipionbox@cnb.csic.es"
EMAILTO="user@domain"
SMTP="localhost"
PUBLISHURL="nolan.cnb.csic.es"
PUBLISHUSER="scipionbox"
PUBLISHCMD="rsync -Lav %(REPORT_FOLDER)s " + "%s@%s:public_html/"%(PUBLISHUSER,PUBLISHURL)
#BACKUPMESSAGE='delete and double click to see mounted disks'
TRANSFERTOOL='/usr/bin/lsyncd'
TRANSFERTOOLARGS=["-nodaemon", "-delay", "300" , "-rsync"]
LATEX_REPORT_TEMPLATE = join(MEDIA_ROOT, 'TEM_report.tex') # in production override
                      # to LATEX_REPORT_TEMPLATE = join(STATIC_ROOT, 'TEM_report.tex')
LATEX_INVOICE_TEMPLATE = join(MEDIA_ROOT, 'TEM_invoice.tex') # override rhis too
LATEX_REPORT_TEMPLATE_ICON = join(MEDIA_ROOT, 'mic.jpg')
LOGIN_REDIRECT_URL = '/'  # after login redirect here
COMPNAME = u"Servicio de Crio-Microscop\\'{i}a"
#export variable to template
HELPURL = 'https://github.com/rmarabini/Talos-User-Guide/wiki/EMserver';

SETTINGS_EXPORT = [
    'HELPURL',
]
##################
# INVOICE SETTINGS
##################
#SITE_NAME = 'MyWebsite'
#AUTH_PROFILE_MODULE = 'myapp.Company'
#INV_MODULE = 'invoice_mod.pdf'
#INV_CURRENCY = ''
#INV_CLIENT_MODULE = 'myapp.Company'

