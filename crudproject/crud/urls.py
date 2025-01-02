from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from.import views

urlpatterns = [
    path('',views.home),
    path('insert',views.insert),
    path('insertTask',views.insertTask),
    path('display',views.display),
    path('delete',views.delete),
    path('deleterec/<int:id>',views.deleterec),
    path('update',views.update),
    path('updatedata/<int:id>',views.updatedata),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
