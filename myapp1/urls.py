from django.urls import path
from myapp1 import views
app_name="myapp1"
urlpatterns = [
    path('',views.index,name='index'),
    path('child',views.child,name='child'),
    path('home',views.home,name="home"),
    
    


]
