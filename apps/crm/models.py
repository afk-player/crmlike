from django.db import models


class Employee(models.Model):
    """Employee model"""
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=25, verbose_name='Employee name')
    surname = models.CharField(max_length=25, verbose_name='Employee surname')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(verbose_name='Employee date of birth', blank=True, null=True)
    country = models.CharField(max_length=25, verbose_name='Employee country')
    email = models.EmailField(verbose_name='Employee email', blank=True, null=True)
    bio = models.TextField(verbose_name='Employee biography', blank=True, null=True)
    employee_photo = models.ImageField(upload_to='employees', blank=True, null=True, verbose_name='Employee photo')
    company = models.ForeignKey('Company', verbose_name='Employee company', on_delete=models.SET_NULL,
                                related_name='employee_company', null=True, blank=True)
    position = models.ForeignKey('Position', verbose_name='Employee position',
                                 on_delete=models.SET_NULL, related_name='employee_position', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class Position(models.Model):
    """Position model"""
    title = models.CharField(max_length=255, verbose_name='Position title', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'


class Company(models.Model):
    """Company model"""
    name = models.CharField(max_length=255, verbose_name='Company name', unique=True)
    country = models.CharField(max_length=25, verbose_name='Company country')
    foundation_date = models.DateField(verbose_name='Company foundation date')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Partnership(models.Model):
    """Partnership model"""
    company = models.OneToOneField(Company, verbose_name='Company', on_delete=models.CASCADE, related_name='company',
                                   unique=True)
    partner = models.ManyToManyField(Company, verbose_name='Company-partner', related_name='company_partner')

    def __str__(self):
        partners = []
        for partner in self.partner.all():
            partners.append(str(partner))
        return 'Company: {}. Partners: {}'.format(self.company, ', '.join(partners))

    class Meta:
        verbose_name = 'Partnership'
        verbose_name_plural = 'Partnerships'
