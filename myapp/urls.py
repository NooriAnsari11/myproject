from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from  . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('intro/', views.intro_page, name='intro_page'),
    path('SignUp/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('intro2/',views.intro2,name='intro2'),
    path('courses/',views.courses,name='courses'),
    path('C11',views.C11,name='C11'),
    path('C12',views.C12,name='C12'),
    path('C13',views.C13,name='C13'),
    path('C21',views.C21,name='C21'),
    path('chapter_completed/<int:chapter_number>/', views.chapter_completed, name='chapter_completed'),
    path('Profile',views.Profile,name='Profile'),
    path('C22',views.C22,name='C22'),
    path('C22a',views.C22a,name='C22a'),
 path('C23',views.C23,name='C23'),
 path('C31',views.C31,name='C31'),
  path('C32',views.C32,name='C32'),
   path('C41',views.C41,name='C41'),
   path('C42',views.C42,name='C42'),
     path('C1',views.C1,name='C1'),


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)