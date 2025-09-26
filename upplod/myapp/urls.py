from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import order_view
    

urlpatterns = [
    
  path('services/', views.services),
   path('submit-order/', order_view, name='order_view'),
        path('',views.SignupPage,name="signup"),
path('login/',views.LoginPage,name="login"), 
path('home/',views.HomePage,name="home"),
path('logout/',views.LogoutPage,name="logout"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)






    
    
