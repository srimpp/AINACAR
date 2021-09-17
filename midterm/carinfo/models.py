from django.db import models

# Create your models here.
class Products(models.Model):
    id = models.IntegerField(), models.AutoField(primary_key=True)
    car_model = models.CharField(db_column='Car_Model', max_length=255, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    min_fe = models.CharField(db_column='Min_FE', max_length=255, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    max_fe = models.CharField(db_column='Max_FE', max_length=255, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    min_pri = models.CharField(db_column='Min_Pri', max_length=255, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    max_pri = models.CharField(db_column='Max_Pri', max_length=255, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    car_type = models.CharField(db_column='Car_Type', max_length=255, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    mcar_infoproducts1aker = models.CharField(db_column='Mcar_infoproducts1aker', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    rdate = models.DateField(db_column='Rdate', blank=True, null=True)  # Field name made lowercase.
    exterior = models.CharField(db_column='Exterior', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    ol = models.CharField(db_column='OL', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    ow = models.CharField(db_column='OW', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    oh = models.CharField(db_column='OH', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    wb = models.CharField(db_column='WB', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    uvw = models.CharField(db_column='UVW', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    limn = models.CharField(db_column='LimN', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    ftc = models.CharField(db_column='FTC', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    tc = models.CharField(db_column='TC', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    eng = models.CharField(db_column='Eng', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    dm = models.CharField(db_column='DM', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    maxp = models.CharField(db_column='MAXP', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    maxor = models.CharField(db_column='MAXOR', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    maxt = models.CharField(db_column='MAXT', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    maxtr = models.CharField(db_column='MAXTR', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    engposi = models.CharField(db_column='EngPosi', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    maxspeed = models.CharField(db_column='MAXSPEED', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    battery = models.CharField(db_column='Battery', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    battery_tyep = models.CharField(db_column='Battery_Tyep', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    tm = models.CharField(db_column='Tm', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    ps = models.CharField(db_column='PS', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    st = models.CharField(db_column='St', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    fw = models.CharField(db_column='FW', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    rw = models.CharField(db_column='RW', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    fts = models.CharField(db_column='FTS', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    rts = models.CharField(db_column='RTS', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    fs = models.CharField(db_column='FS', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    rs = models.CharField(db_column='RS', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    fuel = models.CharField(db_column='Fuel', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    cde = models.CharField(db_column='CDE', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    fcr = models.CharField(db_column='FCR', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    fer = models.CharField(db_column='FER', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.
    fcm = models.CharField(db_column='FCM', max_length=50, db_collation='euckr_korean_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products'
        
        
class CarinfoComments(models.Model):
    id = models.IntegerField(), models.AutoField(primary_key=True)
    carid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)
    rdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carinfo_comments'
        
        