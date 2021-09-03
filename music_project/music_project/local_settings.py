# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q4e8gl)xmg*bm*b%-+&0nct%i5np-=q(+0rq49k^meug!t&=_6'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library',
        'USER': 'root',
        'PASSWORD': 'SoftwareDeveloper101!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
