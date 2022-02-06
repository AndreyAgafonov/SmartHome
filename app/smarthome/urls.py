from django.urls import path

from smarthome.views import index,dashboard, settings

app_name = 'smarthome'

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='index'),
    path('settings/', settings, name='settings'),
    path('settings/<str:settingsMenu>', settings, name='settings'),

    # path('settings/general', settings_general, name='settings_general'),
    # path('settings/dashboard', settings_dashboard, name='settings_dashboard'),
    # path('settings/metrics', settings_metrics, name='settings_metrics'),
    # path('settings/agents', settings_agents, name='settings_agents'),

    # path('new-agent/', settings_ha, name='agentCreate')
]
