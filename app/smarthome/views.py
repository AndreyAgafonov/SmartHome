from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.urls import reverse
import time
from smarthome.models import Rooms, RoomType, SensorsType, SensorsLocate, SensorsDataType, SensorsData, SettingsAgentsConfig,SettingsSections,Settings
from .forms import settingsAgentAddForm, settingsAgentAddForm1, SettingsForm
# from urls import index
def index(request):
    context = {
        'title': "About",

    }
    return render(request, 'smarthome/index.html', context)


# def settings_ha(request):
#     return render(request, 'smarthome/_settings-general.html', )

def settings(request,settingsMenu='general'):
    context = {
        'title': "Settings",
    }
    print(settingsMenu)
    context = {
        'title': "Settings",
        'username': 'Andrey Agafonov'
    }
    settings_menu = SettingsSections.objects.all()

    if request.method == 'POST':
        form = settingsAgentAddForm(request.POST)
        if form.is_valid():

            #ЗАПОЛНЕНИЕ ОБЯЗАТЕЛЬНЫХ ПОЛЕЙ, ЕСЛИ ОНИ НЕ ПЕРЕДАНЫ В ФОРМУ
            # author = Author(title='Mr')
            # form = PartialAuthorForm(request.POST, instance=author)
            # form.save()

            print(form.cleaned_data)
            agentconfig = SettingsAgentsConfig.objects.update_or_create(**form.cleaned_data)
            print(agentconfig)
            return redirect(reverse('smarthome:index'))
    if request.method == 'GET':

        form = SettingsForm()

    for section in settings_menu:
        if settingsMenu.lower() == section.name.lower():
            return render(request, 'smarthome/settings.html', {'context': context, 'settingsMenu': settingsMenu, 'settings_menu': settings_menu, 'settingsMenu': settingsMenu, 'form': form})
    return redirect('smarthome:settings')


# def settings_agents(request):
#     if request.method == 'POST':
#         form = settingsAgentAddForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             agentconfig = SettingsAgentsConfig.objects.update_or_create(**form.cleaned_data)
#             print(agentconfig)
#             return redirect(reverse('smarthome:index'))
#     if request.method == 'GET':
#         context = {
#             'title': "Settings",
#             'username': 'Andrey Agafonov',
#             'agentList': SettingsAgentsConfig.objects.all()
#         }
#         form = settingsAgentAddForm()
#         settings_menu = SettingsSections.objects.all()
#     return render(request, 'smarthome/_settings-agents.html', {'settings_menu': settings_menu, 'context': context, 'form': form})
#
# def settings_metrics(request):
#     settings_menu = SettingsSections.objects.all()
#     return render(request, 'smarthome/_settings-metrics.html', {'settings_menu': settings_menu})

def dashboard(request):
    rooms = Rooms.objects.all()
    room_list = []

    for room in rooms:
        sensors_in_room = []
        sensorsList = SensorsLocate.objects.filter(room_id=room.id)
        for sensor in sensorsList:
            sensors_in_room.append( {
                'name': sensor.short_description,
                'image': SensorsType.objects.filter(id=sensor.sensor_id).latest('id').image,
                'value': SensorsData.objects.filter(sensorName_id=sensor.id).latest('timestamp').value,
                'unit': SensorsType.objects.filter(id=sensor.sensor_id).latest('id').unit,
                'description': ""
            })
        room_list.append( {
            'name': room.name,
            'image': room.image,
            'roomType': RoomType.objects.filter(id=room.roomType_id).latest('id').name,
            'friendlyName':room.friendlyName,
            'description': room.description,
            'sensors': sensors_in_room
        }
        )
    context = {
        'title': "dashboard",
        'rooms': room_list
    }
    return render(request, 'smarthome/dashboard.html', context)