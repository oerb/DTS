from django.db import models

"""
Hausmeister Arbeitszeiterfassung
"""
class Work_Interval(models.Model):
    """Work_Interval model."""
    TYP_CHOICES = (
        (1, 'Week'),
        (2, 'Month'),
        (3, 'Year'),
    )
    name = models.CharField(u'Name', max_length=100, blank=False, null=False)
    description = models.CharField(u'Description', max_length=250, blank=True, null=True)
    typ = models.IntegerField(choices=TYP_CHOICES, default=1)


class Worktyp(models.Model):
    """Worktyp model."""
    name = models.CharField(u'Name', max_length=100, blank=False, null=False)
    Description = models.CharField(u'Description', max_length=250, blank=True, null=True)
    billable = models.BooleanField(u'Abrechenbar', default=False)
    WTintervall = models.ManyToManyField(Work_Interval, verbose_name='Work-Interval')


class Worktime(models.Model):
    """ Worktime model."""
    subject = models.CharField(u'Subject', max_length=255)
    location = models.CharField(u'Location', max_length=255)
    start_time = models.DateTimeField(u'StartTime', blank=False, null=False)
    end_time = models.DateTimeField(u'EndTime', blank=False, null=False)
    start_date = models.DateField(u'StartDate')
    end_date = models.DateField(u'EndDate')
    body = models.TextField(u'Body', blank=False, null=False)
    mandant = models.IntegerField(u'Mandant', blank=False, null=False)
    unternehmen = models.IntegerField(u'Unternehmen', blank=False, null=False)
    we = models.IntegerField(u'WE', blank=False, null=False)
    ne = models.IntegerField(u'NE', blank=False, null=False)
    mieter = models.IntegerField(u'Mieter', blank=False, null=False)
    WTworktyp = models.ManyToManyField(Worktyp, verbose_name='Work-Typ', blank=False, null=False)


