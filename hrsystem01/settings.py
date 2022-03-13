"""
Django settings for hrsystem01 project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=3@y+*gm!ry9^bzip*i4mu+#uaj!r)%qzj#-q$dd(jo&*_@wp#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
#🌟お問い合わせメール送信アドレスと件名のsubメッセージ削除
#DEFAULT_FROM_EMAIL = 'support@hurebook.com'
#ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

# Application definition

INSTALLED_APPS = [
    #'accounts'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hrsystem01.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hrsystem01.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
#AUTH_USER_MODEL = 'accounts.CustomUser'
#SITE_ID = 1

#AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.ModelBackend', #デフォルトの認証基盤
#    'allauth.account.auth_backends.AuthenticationBackend' # メールアドレスとパスワードの両方を用いて認証するために必要
#)

#ACCOUNT_AUTHENTICATION_METHOD = 'email' # メールアドレス（とパスワードで）認証する
#ACCOUNT_USERNAME_REQUIRED = True # サインアップ（ユーザー登録）の時にユーザーネームを尋ねる
#ACCOUNT_EMAIL_REQUIRED = True # サインアップ（ユーザー登録）の時にメールアドレスを尋ねる
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory' # メール検証を必須とする
 
#LOGIN_URL = '/account/login/' # ログインURLの設定
#LOGIN_REDIRECT_URL = ' ' # ログイン後のリダイレクト先
#ACCOUNT_LOGOUT_REDIRECT_URL = '/account/login/' #　ログアウト後のリダイレクト先
#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'