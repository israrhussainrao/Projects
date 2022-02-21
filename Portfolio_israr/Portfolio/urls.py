from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sendmail', views.sendmail, name="sendmail"),
    path('project/<int:pk>', views.project, name="project"),
    path('projects', views.projects, name="projects"),
    path('blog/<int:pk>', views.blog, name="blog"),
    path('blogs', views.blogs, name="blogs"),
]

handler404 = 'Portfolio.views.custom_page_not_found_view'
handler500 = 'Portfolio.views.custom_error_view'
handler403 = 'Portfolio.views.custom_permission_denied_view'
handler400 = 'Portfolio.views.custom_bad_request_view'
