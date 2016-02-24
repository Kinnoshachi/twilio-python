# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import serialize
from twilio import values
from twilio.instance_context import InstanceContext
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page


class WorkersStatisticsList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkersStatisticsList
        
        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        
        :returns: WorkersStatisticsList
        :rtype: WorkersStatisticsList
        """
        super(WorkersStatisticsList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
        }

    def get(self):
        """
        Constructs a WorkersStatisticsContext
        
        :returns: WorkersStatisticsContext
        :rtype: WorkersStatisticsContext
        """
        return WorkersStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __call__(self):
        """
        Constructs a WorkersStatisticsContext
        
        :returns: WorkersStatisticsContext
        :rtype: WorkersStatisticsContext
        """
        return WorkersStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkersStatisticsList>'


class WorkersStatisticsPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the WorkersStatisticsPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid
        
        :returns: WorkersStatisticsPage
        :rtype: WorkersStatisticsPage
        """
        super(WorkersStatisticsPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkersStatisticsInstance
        
        :param dict payload: Payload response from the API
        
        :returns: WorkersStatisticsInstance
        :rtype: WorkersStatisticsInstance
        """
        return WorkersStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkersStatisticsPage>'


class WorkersStatisticsContext(InstanceContext):

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkersStatisticsContext
        
        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        
        :returns: WorkersStatisticsContext
        :rtype: WorkersStatisticsContext
        """
        super(WorkersStatisticsContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workers/Statistics'.format(**self._solution)

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset, task_queue_sid=values.unset,
              task_queue_name=values.unset, friendly_name=values.unset):
        """
        Fetch a WorkersStatisticsInstance
        
        :param unicode minutes: The minutes
        :param datetime start_date: The start_date
        :param datetime end_date: The end_date
        :param unicode task_queue_sid: The task_queue_sid
        :param unicode task_queue_name: The task_queue_name
        :param unicode friendly_name: The friendly_name
        
        :returns: Fetched WorkersStatisticsInstance
        :rtype: WorkersStatisticsInstance
        """
        params = values.of({
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'EndDate': serialize.iso8601_datetime(end_date),
            'TaskQueueSid': task_queue_sid,
            'TaskQueueName': task_queue_name,
            'FriendlyName': friendly_name,
        })
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return WorkersStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkersStatisticsContext {}>'.format(context)


class WorkersStatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid):
        """
        Initialize the WorkersStatisticsInstance
        
        :returns: WorkersStatisticsInstance
        :rtype: WorkersStatisticsInstance
        """
        super(WorkersStatisticsInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'cumulative': payload['cumulative'],
            'realtime': payload['realtime'],
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid,
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: WorkersStatisticsContext for this WorkersStatisticsInstance
        :rtype: WorkersStatisticsContext
        """
        if self._context is None:
            self._context = WorkersStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def cumulative(self):
        """
        :returns: The cumulative
        :rtype: unicode
        """
        return self._properties['cumulative']

    @property
    def realtime(self):
        """
        :returns: The realtime
        :rtype: unicode
        """
        return self._properties['realtime']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset, task_queue_sid=values.unset,
              task_queue_name=values.unset, friendly_name=values.unset):
        """
        Fetch a WorkersStatisticsInstance
        
        :param unicode minutes: The minutes
        :param datetime start_date: The start_date
        :param datetime end_date: The end_date
        :param unicode task_queue_sid: The task_queue_sid
        :param unicode task_queue_name: The task_queue_name
        :param unicode friendly_name: The friendly_name
        
        :returns: Fetched WorkersStatisticsInstance
        :rtype: WorkersStatisticsInstance
        """
        return self._proxy.fetch(
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
            task_queue_sid=task_queue_sid,
            task_queue_name=task_queue_name,
            friendly_name=friendly_name,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkersStatisticsInstance {}>'.format(context)
