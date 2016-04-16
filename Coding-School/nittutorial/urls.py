from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.home, name='tut1'),
    url(r'^nittutorial/$',views.tut1, name='tut1'),
    url(r'^forums/',views.forums, name='tut1'),
    url(r'^blogs/',views.blogs, name='tut1'),
    url(r'^contributors/',views.contributors, name='tut1'),
    url(r'^about/',views.about, name='tut1'),
    url(r'^contact/',views.contact, name='tut1'),
    url(r'^reg/',views.manage_authors, name='manage_authors'),
    url(r'^nittutorial/(?P<title>.+)/(?P<id>\d+)/$',views.post_content, name='post_content'),
    url(r'^new/', views.tutorial_new, name='tutorial_new'),  
    url(r'^cf_profile/',views.cf_profile, name='tut1'),
    url(r'^cf_form/',views.cf_form, name='tut1'),
    url(r'^problems_find/',views.problems_find, name='tut1'),
    url(r'^problems_display/',views.problems_display, name='tut1'),
    url(r'^compile/',views.compile, name='tut1'),
    url(r'^run/',views.run, name='tut1'),
    url(r'^editor/',views.editor, name='tut1'),
]