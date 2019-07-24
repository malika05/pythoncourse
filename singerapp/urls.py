from django.urls import path
from singerapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    path('labels', views.LabelsView.as_view()),
    path('labels/<int:pk>', views.LabelsDetailView.as_view()),
    path('groups', views.GroupsView.as_view()),
    path('groups/<int:pk>', views.GroupsDetailView.as_view()),
    path('feedback', views.FeedbackView.as_view()),
    path('feedback/<int:pk>', views.FeedbackDetailView.as_view()),
    path('singers', views.SingersView.as_view()),
    path('singers/<int:pk>', views.SingersDetailView.as_view()),
    path('solo_singer', views.Solo_singerView.as_view()),
    path('solo_singer/<int:pk>', views.Solo_singerDetailView.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth', include('rest_framework.urls')),
]