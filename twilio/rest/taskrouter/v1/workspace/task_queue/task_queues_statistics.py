# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class StatisticsList(ListResource):

    def __init__(self, version, workspace_sid):
        super(StatisticsList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/TaskQueues/Statistics".format(**self._kwargs)

    def read(self, end_date=values.unset, friendly_name=values.unset,
             minutes=values.unset, start_date=values.unset, limit=None,
             page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            "EndDate": end_date,
            "FriendlyName": friendly_name,
            "Minutes": minutes,
            "StartDate": start_date,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            StatisticsInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, end_date=values.unset, friendly_name=values.unset,
             minutes=values.unset, start_date=values.unset, page_token=None,
             page_number=None, page_size=None, **kwargs):
        params = values.of({
            "EndDate": end_date,
            "FriendlyName": friendly_name,
            "Minutes": minutes,
            "StartDate": start_date,
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            StatisticsInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self):
        return StatisticsContext(self._version, **self._kwargs)

    def __repr__(self):
        return '<Twilio.Taskrouter.V1.StatisticsList>'


class StatisticsContext(InstanceContext):

    def __init__(self, version):
        super(StatisticsContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = "None".format(**self._kwargs)


class StatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid):
        super(StatisticsInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'cumulative': payload['cumulative'],
            'realtime': payload['realtime'],
            'task_queue_sid': payload['task_queue_sid'],
            'worker_sid': payload['worker_sid'],
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'workspace_sid': workspace_sid,
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = StatisticsContext(
                self._version,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def cumulative(self):
        """ The cumulative """
        return self._properties['cumulative']

    @property
    def realtime(self):
        """ The realtime """
        return self._properties['realtime']

    @property
    def task_queue_sid(self):
        """ The task_queue_sid """
        return self._properties['task_queue_sid']

    @property
    def worker_sid(self):
        """ The worker_sid """
        return self._properties['worker_sid']

    @property
    def workspace_sid(self):
        """ The workspace_sid """
        return self._properties['workspace_sid']