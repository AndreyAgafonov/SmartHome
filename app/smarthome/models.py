from django.db import models

# Create your models here.
class RoomType(models.Model):
    class Meta:
        verbose_name_plural = 'Type of Rooms'

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Rooms(models.Model):
    class Meta:
        verbose_name_plural = 'Rooms'

    name = models.CharField(max_length=64, unique=True)
    friendlyName = models.CharField(max_length=64, unique=True)
    image = models.ImageField(upload_to='smarthome_images',blank=True)
    roomType = models.ForeignKey(RoomType, on_delete=models.PROTECT)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} |{self.roomType}'



class SensorsDataType(models.Model):
    class Meta:
        verbose_name_plural = 'Type of Data from Sensors'

    name = models.CharField(max_length=64, unique=True)
    friendlyName=models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.friendlyName



class SensorsType(models.Model):
    class Meta:
        verbose_name_plural = 'Type of Sensors'
        # unit = {SensorsType.unit}
    name = models.CharField(max_length=64, unique=True)
    image = models.ImageField(upload_to='smarthome_images',blank=True)
    short_description = models.CharField(max_length=64,blank=True)
    category = models.ForeignKey(SensorsDataType, on_delete=models.PROTECT)
    unit = models.CharField(max_length=8, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}, {self.unit} | {self.category.friendlyName}'


class SensorsLocate(models.Model):
    class Meta:
        verbose_name_plural = 'Sensors Locate'
    # name = models.CharField(max_length=64, unique=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    sensor = models.ForeignKey(SensorsType, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.room.name} | {self.short_description}'

class SensorsData(models.Model):
    class Meta:
        verbose_name_plural = 'Sensors Data'

    timestamp = models.DateTimeField(blank=False)
    sensorName = models.ForeignKey(SensorsLocate, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return f'{self.timestamp} - {self.sensorName} - {self.value}'


class SettingsAgentsConfig(models.Model):
    class Meta:
        verbose_name_plural: 'Settings Agent Conig'

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=50,unique=True,blank=False)
    sshUser = models.CharField(max_length=20, blank=False)
    sshPrivateKey = models.TextField(max_length=4120, blank=True)
    def __str__(self):
        return f'{self.name}| {self.address}'


class SettingsSections(models.Model):
    class Meta:
        verbose_name_plural: 'Settings Sections'

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    output_number = models.IntegerField(unique=True, blank=False)
    url_name = models.CharField(max_length=64, unique=False, blank=False)
    def __str__(self):
        return f'{self.output_number} - {self.name}'

class SettingsType(models.Model):
    class Meta:
        verbose_name_plural: 'Settings Type'

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=16, unique=True, blank=False)
    def __str__(self):
        return f'{self.name}'

class Settings(models.Model):
    class Meta:
        verbose_name_plural: 'Settings'

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    settingsSection = models.ForeignKey(SettingsSections,on_delete=models.CASCADE)
    settingsType = models.ForeignKey(SettingsType, on_delete=models.CASCADE)
    settingsValueString = models.CharField(max_length=128,blank=True,unique=False)
    settingsValueBoolean = models.BooleanField(blank=True)
    def __str__(self):
        return f'{self.settingsSection} {self.name} {self.settingsType}'