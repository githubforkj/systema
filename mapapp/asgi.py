import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mapapp.settings')

application = get_asgi_application()

#デフォルトで存在しなかったため、手動で作成しました。
