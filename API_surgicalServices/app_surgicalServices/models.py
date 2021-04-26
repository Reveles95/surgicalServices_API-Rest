from django.db import models

class Services(models.Model):
    service_Name = models.CharField(max_length=100, blank=False)
    service_Description = models.CharField(max_length=1100, blank=False)
    phone = models.IntegerField(blank=False)
    mail = models.EmailField(blank=False)
    adress = models.CharField(max_length=100, blank=False)
    team = models.CharField(max_length=150, blank=False)
    
    def __str__(self):
        return self.service_Name

specialist_Expertise = [
    ('E1', 'Cirugía Baríatrica'),
    ('E2', 'Obesidad'),
    ('E3', 'Trastornos de la Alimentación'),
    ('E4', 'Psicología de Salud'),
]

specialist_Gender = [
    ('Male', 'M'),
    ('Female', 'F'),
]

class specialistsTeam(models.Model):
    Name = models.CharField(max_length=50, blank=False)
    Last_Name = models.CharField(max_length=50, blank=False)
    Code = models.CharField(max_length=8, blank=False)
    Expertise = models.CharField(max_length=100, choices=specialist_Expertise, default='select expertise')
    Gender = models.CharField(max_length=50, choices=specialist_Gender, default='select gender')
    About = models.CharField(max_length=1100, blank=False)
    specialist_Services = models.CharField(max_length=1100, blank=False)
    Adress = models.CharField(max_length=100, blank=False)
    Edu = models.CharField(max_length=300, blank=False)
    fk_Services = models.OneToOneField(Services, on_delete=models.CASCADE, blank=False)
    
    def __str__(self):
        return self.specialist_Expertise


