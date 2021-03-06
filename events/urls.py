from django.conf.urls import include, url

from events.views import (ArchiveView, EventDetailView, AttendanceView,
        latest_event_detail)
from polls.views import EventPollView, EventPollResultsView


urlpatterns = [
    url(r'^$', latest_event_detail, name="event_latest"),
    url(r'^archive/$', ArchiveView.as_view(), name="event_archive"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        EventDetailView.as_view(), kwargs={'slug': ''},
        name="event_detail"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/attendance/$',
        AttendanceView.as_view(), kwargs={'slug': ''},
        name="event_attendance"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/poll/$',
        EventPollView.as_view(), kwargs={'slug': ''},
        name="event_poll"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/poll/results/$',
        EventPollResultsView.as_view(), kwargs={'slug': ''},
        name="event_poll_results"),
]
