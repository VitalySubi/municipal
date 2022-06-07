from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DiagEquipment(models.Model):
    diaid = models.AutoField(primary_key=True)
    dianame = models.CharField(max_length=255, blank=True, null=True)
    diatype = models.CharField(max_length=255, blank=True, null=True)
    diadate = models.DateField(blank=True, null=True)
    diaplace = models.CharField(max_length=255, blank=True, null=True)
    diaenable = models.BooleanField(blank=True, null=True)
    diacount_research = models.IntegerField(blank=True, null=True)
    diavolume_research = models.FloatField(blank=True, null=True)
    diadicom = models.BooleanField(blank=True, null=True)
    diaactivate = models.BooleanField(blank=True, null=True)
    diaarm_diag = models.BooleanField(blank=True, null=True)
    tvsd = models.ForeignKey('Tvsp', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diag_equipment'


class Equipment(models.Model):
    equid = models.AutoField(primary_key=True)
    equcabinet = models.IntegerField(blank=True, null=True)
    netid = models.ForeignKey('NetInfTvsp', models.DO_NOTHING, db_column='netid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment'


class InfoSystem(models.Model):
    infid = models.AutoField(primary_key=True)
    infname = models.CharField(max_length=255, blank=True, null=True)
    ingtype = models.CharField(max_length=255, blank=True, null=True)
    infdeveloper = models.CharField(max_length=255, blank=True, null=True)
    infenemy = models.CharField(max_length=255, blank=True, null=True)
    infcert = models.IntegerField(blank=True, null=True)
    infgis = models.BooleanField(blank=True, null=True)
    infobjkii = models.BooleanField(blank=True, null=True)
    infcat = models.CharField(max_length=255, blank=True, null=True)
    munid = models.ForeignKey('MunicipInstit', models.DO_NOTHING, db_column='munid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_system'


class InternetAccess(models.Model):
    intid = models.AutoField(primary_key=True)
    intstat = models.CharField(max_length=255, blank=True, null=True)
    inttech = models.CharField(max_length=255, blank=True, null=True)
    intchanel = models.CharField(max_length=255, blank=True, null=True)
    inttarif = models.CharField(max_length=255, blank=True, null=True)
    intsupl = models.CharField(max_length=255, blank=True, null=True)
    intprice = models.FloatField(blank=True, null=True)
    intfp = models.BooleanField(blank=True, null=True)
    netid = models.ForeignKey('NetInfTvsp', models.DO_NOTHING, db_column='netid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internet_access'


class Keyboard(models.Model):
    model = models.CharField(max_length=255, blank=True, null=True)
    date_buy = models.DateField(blank=True, null=True)
    inv = models.IntegerField(blank=True, null=True)
    equipmentid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='equipmentid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyboard'


class LocalNet(models.Model):
    locid = models.AutoField(primary_key=True)
    loccount = models.IntegerField(blank=True, null=True)
    loceq = models.CharField(max_length=255, blank=True, null=True)
    locip = models.CharField(max_length=255, blank=True, null=True)
    locserver = models.BooleanField(blank=True, null=True)
    locareasize = models.FloatField(blank=True, null=True)
    loclocation = models.CharField(max_length=255, blank=True, null=True)
    loctreb = models.BooleanField(blank=True, null=True)
    locschema = models.CharField(max_length=255, blank=True, null=True)
    netid = models.ForeignKey('NetInfTvsp', models.DO_NOTHING, db_column='netid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_net'


class Monitor(models.Model):
    monid = models.AutoField(primary_key=True)
    monmodel = models.CharField(max_length=255, blank=True, null=True)
    mondiag = models.CharField(max_length=10, blank=True, null=True)
    moninv = models.CharField(max_length=255, blank=True, null=True)
    mondate = models.DateField(blank=True, null=True)
    equid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='equid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor'


class Mouse(models.Model):
    model = models.CharField(max_length=255, blank=True, null=True)
    date_buy = models.DateField(blank=True, null=True)
    inv = models.IntegerField(blank=True, null=True)
    equipmentid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='equipmentid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mouse'


class MunicipInstit(models.Model):
    munid = models.AutoField(primary_key=True)
    munname = models.CharField(max_length=255, blank=True, null=True)
    munaddr = models.CharField(max_length=255, blank=True, null=True)
    munoid = models.IntegerField(blank=True, null=True)
    munlevel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municip_instit'


class NetInfTvsp(models.Model):
    netid = models.AutoField(primary_key=True)
    tvsid = models.ForeignKey('Tvsp', models.DO_NOTHING, db_column='tvsid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'net_inf_tvsp'


class ProtectedNet(models.Model):
    defid = models.AutoField(primary_key=True)
    defstatus = models.BooleanField(blank=True, null=True)
    deftech = models.CharField(max_length=255, blank=True, null=True)
    defvipcoord = models.CharField(max_length=255, blank=True, null=True)
    defviphw = models.CharField(max_length=255, blank=True, null=True)
    defvipclient = models.CharField(max_length=255, blank=True, null=True)
    netid = models.ForeignKey(NetInfTvsp, models.DO_NOTHING, db_column='netid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protected_net'


class Software(models.Model):
    sofid = models.AutoField(primary_key=True)
    sofname = models.CharField(max_length=255, blank=True, null=True)
    sofdeveloper = models.CharField(max_length=255, blank=True, null=True)
    sofrussian = models.BooleanField(blank=True, null=True)
    sofversion = models.CharField(max_length=10, blank=True, null=True)
    sofprice = models.FloatField(blank=True, null=True)
    sofdate = models.DateField(blank=True, null=True)
    equid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='equid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'software'


class SysBlock(models.Model):
    sysid = models.AutoField(primary_key=True)
    sysdata = models.DateField(blank=True, null=True)
    sysinv = models.CharField(max_length=255, blank=True, null=True)
    sysmodel = models.CharField(max_length=255, blank=True, null=True)
    sysmodram = models.CharField(max_length=255, blank=True, null=True)
    sysvolram = models.CharField(max_length=10, blank=True, null=True)
    systypehold = models.CharField(max_length=255, blank=True, null=True)
    sysvolumehold = models.CharField(max_length=10, blank=True, null=True)
    sysmodelhold = models.CharField(max_length=255, blank=True, null=True)
    sysos = models.CharField(max_length=255, blank=True, null=True)
    equid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='equid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_block'


class Tvsp(models.Model):
    tvsid = models.AutoField(primary_key=True)
    tvsname = models.CharField(max_length=255, blank=True, null=True)
    tvstype = models.CharField(max_length=255, blank=True, null=True)
    tvsaddress = models.CharField(max_length=255, blank=True, null=True)
    tvsoid = models.IntegerField(blank=True, null=True)
    tvsambulance = models.BooleanField(blank=True, null=True)
    tvspmsp = models.BooleanField(blank=True, null=True)
    tvsregist = models.BooleanField(blank=True, null=True)
    tvsstation = models.BooleanField(blank=True, null=True)
    tvskdl = models.BooleanField(blank=True, null=True)
    tvssmp = models.BooleanField(blank=True, null=True)
    tvsnmp = models.BooleanField(blank=True, null=True)
    tvsinstrdiag = models.BooleanField(blank=True, null=True)
    tvsllo = models.BooleanField(blank=True, null=True)
    tvsmse = models.BooleanField(blank=True, null=True)
    tvslist = models.BooleanField(blank=True, null=True)
    tvsssz = models.BooleanField(blank=True, null=True)
    tvscoord = models.TextField(blank=True, null=True)  # This field type is a guess.
    tvsfloor = models.IntegerField(blank=True, null=True)
    tvsform = models.CharField(max_length=255, blank=True, null=True)
    tvsstatus = models.CharField(max_length=255, blank=True, null=True)
    tvsplan = models.CharField(max_length=255, blank=True, null=True)
    munid = models.ForeignKey(MunicipInstit, models.DO_NOTHING, db_column='munid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tvsp'
