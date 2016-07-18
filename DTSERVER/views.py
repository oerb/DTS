
__author__ = 'Bjoer Leppin'
__copyright__ = 'Copyright 2016, Björn Leppin'
__email__ = 'bjoern@oerb.de'
__license__ = "privat"
__status__ = "Alpha"

from django.contrib.auth.models import User, Group
from DTSERVER.models import Worktime, Worktyp, Work_Interval
from rest_framework import viewsets
from DTSERVER.serializers import WorkIntervalSerializer, WorktimeSerializer, \
    WorktypSerializer, UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class Work_IntervalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows WorkInterval to be viewed or edited.
    """
    queryset = Work_Interval.objects.all()
    serializer_class = WorkIntervalSerializer


class WorktypViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Worktyp to be viewed or edited.
    """
    queryset = Worktyp.objects.all()
    serializer_class = WorktypSerializer


class WorktimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Worktime to be viewed or edited.
    """
    queryset = Worktime.objects.all()
    serializer_class = WorktimeSerializer

