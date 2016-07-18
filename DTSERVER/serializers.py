__author__ = 'Bjoer Leppin'
__copyright__ = 'Copyright 2016, Björn Leppin'
__email__ = 'bjoern@oerb.de'
__license__ = "privat"
__status__ = "Alpha"


from django.contrib.auth.models import User, Group
from rest_framework import serializers
from DTSERVER.models import Work_Interval, Worktyp, Worktime

"""
Login
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


"""
Hausmeister Arbeitszeiterfassung #Serializers
"""

class WorkIntervalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work_Interval
        fields = ('name', 'description', 'typ')


class WorktypSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worktyp
        fields = ('name', 'Description', 'billable', 'WTintervall')


class WorktimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worktime
        fields = ('subject', 'location', 'start_time', 'end_time',
                  'start_date', 'end_date', 'body', 'mandant',
                  'unternehmen', 'we', 'ne', 'mieter', 'WTworktyp')