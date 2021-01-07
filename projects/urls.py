from django.urls import path

from projects.views import HookReceiverView

urlpatterns = [
    path('hooks/<uuid:uuid>', HookReceiverView.as_view()),

]
