
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-_^v(h2h)(fb0elp020dw2&or^3tp&3fz7sr7)h$3j8)-d+l=@2'


DEBUG = True

ALLOWED_HOSTS = ['*']




INSTALLED_APPS = [
    'website',
    'tinymce',
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

ROOT_URLCONF = 'dtrans.urls'

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

WSGI_APPLICATION = 'dtrans.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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




LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True




STATIC_URL = 'static/'
STATIC_ROOT = 'static/'
MEDIA_URL = 'drans/media/'
MEDIA_ROOT = 'drans/media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TINYMCE_DEFAULT_CONFIG = {
    'valid_elements': '*[*]',  # Разрешить все HTML-теги и атрибуты
    'forced_root_block': 'p',  # Сохраняем текст в <p>
    'height': 300,
    'width': '100%',
    'menubar': True,
    'plugins': 'textcolor link image media preview codesample table charmap hr pagebreak lists paste',
    'toolbar': 'undo redo | bold italic underline | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent | numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | image media template link anchor codesample | ltr rtl',
    'setup': '''function(editor) {
        editor.on('NodeChange', function(e) {
            if (e && e.element.nodeName === 'IMG') {
                e.element.style.height = '100%';
                e.element.style.width = '100%';
                e.element.style.objectFit = 'cover';
                e.element.style.borderRadius = '16px';
            }
        });
    }'''
}