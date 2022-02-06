from django.contrib import admin
from smarthome.models import SensorsDataType, SensorsType, Rooms,SensorsData, RoomType,SensorsLocate, SettingsAgentsConfig, SettingsSections, SettingsType, Settings
# Register your models here.

admin.site.register(SensorsDataType)
admin.site.register(SensorsType)

admin.site.register(Rooms)
admin.site.register(RoomType)

admin.site.register(SensorsData)
admin.site.register(SensorsLocate)

admin.site.register(SettingsAgentsConfig)
admin.site.register(SettingsSections)
admin.site.register(SettingsType)
admin.site.register(Settings)

