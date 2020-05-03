from django.test import TestCase

# Create your tests here.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('managements/', include('managements.urls', namespace='managements')),
    path('runners/', include('runners.urls', namespace='runners')),
    # path('a/', 'views.user_view.')
    # path('docs/', schema_view, name='docs')
]

if __name__ == '__main__':
    path_string = urlpatterns[0]
    print(path_string)
    pass
