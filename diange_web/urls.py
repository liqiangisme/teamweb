from django.conf.urls import url
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$',views.home),
    #url(r'^(\d+)/$',views.detail),

    #url(r'^grade/$',views.gra),
    #url(r'^student/$',views.stu),
    #url(r'^grade/(\d+)$',views.gradeStudent),
    #url(r'^grade/member/$',views.member),
]