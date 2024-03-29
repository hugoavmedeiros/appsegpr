import os, inspect
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-39@rq#r0otq)x^$p4tjf70da5%vol#m=yw3cvi(1i1=+#*3wmq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ['https://*.seplag.pe.gov.br', 'https://*.127.0.0.1']
ALLOWED_HOSTS = ['10.238.75.122', 'https://*.seplag.pe.gov.br', '127.0.0.1']
CSRF_COOKIE_SECURE = False


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'planos',
    'reunioes',
    'apoio',
    'orcamento',
    'orgaos',    
    'import_export',
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

ROOT_URLCONF = 'sitePainel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
        ],
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

WSGI_APPLICATION = 'sitePainel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


STATIC_ROOT = ''
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'apoio', 'static'),
    'static', 
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "filters_position": "right",
    "site_title": "SEGPR",
    "site_header": "SEGPR", 
    "site_brand": " ",
    "site_logo": "imagens/seplagtransparente_32.png",
    "site_logo_classes": "squared",
    "login_logo": "imagens/seplagtransparente_login.png",
    "site_icon": "imagens/favicon.png",
    "welcome_sign": "Bem-vindo(a)",
    "copyright": "Secretaria de Planejamento, Gestão e Desenvolvimento Regional de Pernambuco",
    "topmenu_links": [
        {"name": "Início",  "url": "apoio:index", "permissions": ["auth.view_user"]},
        {"name": "Suporte", "url": "https://www.seplag.pe.gov.br/contato", "new_window": True},
        {"model": "auth.User"},
        {"app": "appPainel"},
    ],
    "order_with_respect_to": [
        "auth", 
        "planos.Plano",
        "planos.AcaoPlano",
        "reunioes.Reuniao",
        "reunioes.Encaminhamento",
        "apoio.Ano",
        "apoio.EixoPlano",
        "apoio.TipoPrograma",
        "apoio.TipoAcao",
        ],
    "show_ui_builder": False,
    
    ##BUSCA
    #"search_bar": True,
    #"search_model": ["appPainel.Meta"],
    
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "collapsible",
    },
    #### BARRA LATERAL ####

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "apoio.EixoPlano": "fas fa-network-wired",
        "apoio.Municipio": "fas fa-city",
        "orgaos.AIS": "fas fa-map",
        "orgaos.Responsavel": "fas fa-user-tie",
        "orgaos.Secretaria": "fas fa-building",
        "orgaos.Orgao": "fas fa-house-flag",
        "planos.Plano": "fas fa-list",
        "planos.AcaoPlano": "fas fa-check-double",
        "reunioes.Reuniao": "fas fa-handshake",
        "reunioes.Encaminhamento": "fas fa-calendar-check",
    },
    
    "default_icon_children": "fas fa-square",

    "show_sidebar": True,
    "navigation_expanded": False,
    #"search_models": [
    #    {"app": "appPainel", "model": "Meta"},
    #],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-navy",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": 'sidebar-light-navy',
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    #"theme": "sandstone",
    "theme": "sandstone",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-primary"
    },
    "actions_sticky_top": True
}

QUERY_URL = True