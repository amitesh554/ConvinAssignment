from django.shortcuts import render
from django.views.generic import TemplateView
from oauth2client import client, flow


class GoogleCalendarInitView(TemplateView):
    def get(self, request):
        flow = client.flow_from_clientsecrets(
            'client_secret.json',
            scope='https://www.googleapis.com/auth/calendar')
        auth_url = flow.step1_get_authorization_url()
        return redirect(auth_url)


class GoogleCalendarRedirectView(TemplateView):
    def get(self, request):
        code = request.GET.get('code')
        flow = client.flow_from_clientsecrets(
            'client_secret.json',
            scope='https://www.googleapis.com/auth/calendar')
        credentials = flow.step2_exchange(code)
        access_token = credentials.access_token
        events = client.Calendar().events().list(
            calendarId='primary', access_token=access_token).execute()
        return render(request, 'google_calendar.html', {'events': events})
