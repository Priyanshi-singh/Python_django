from django.db.models import *

# model #shortcut to create model

class Movies(Model):
    title = CharField(max_length=50)
    year = IntegerField()
    rating = FloatField()

    def __str__(self):
        return self.title

class Show(Model):
    title = CharField(max_length=60)
    year=IntegerField()
    season_count=IntegerField()
    rating = FloatField()
    created_at = DateTimeField(auto_now=True)

class Student(Model):
    name = CharField(max_length=50)
    klass = IntegerField(verbose_name='class')
    roll_no = IntegerField(verbose_name = 'roll number')
class Report(Model):
    english = IntegerField()
    maths = IntegerField()
    science = IntegerField()
    computer = IntegerField()
    hindi = IntegerField()
    student = ForeignKey('student', on_delete = DO_NOTHING)

    def __str__(self) -> str:
        return f'Report of {self.student.name}'

class Weather(Model):
    temp = DecimalField(verbose_name = 'temp(C)',max_digits=5,decimal_places=2)
    wind_speed = DecimalField()
    humidity = DecimalField()
    date = DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.temp

