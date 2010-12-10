"""
Sends an HTML email to all team members in the ``team`` list. The tabular view
provides the story title/url, show the story is assigned to, and started or
unstarted state.  This contains stories across all projects the team member is
assigned to.

Hook this up to a cron job for periodic (e.g. daily on weekdays) emails.
"""
import datetime

from pivotal import Pivotal

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template

# To use Django as a library
settings.configure()

team = [
    {'email': 'someone@example.com',
     'token': 't0k3n'},
    # ...
]

def xml_get(node, field, default=''):
    try:
        return node.find(field).text
    except AttributeError:
        return ''

for person in team:
    pv = Pivotal(person['token'])

    data = {}

    xml = pv.projects().get_etree()
    for proj in xml.getchildren():
        proj_name = proj.find('name').text
        data[proj_name] = []
        id = int(proj.find('id').text)
        qs = {
            'filter': 'state:started',
        }
        xml = pv.projects(id).stories(**qs).get_etree()
        for story in xml.getchildren():
            data[proj_name].append({
                'name': xml_get(story, 'name'),
                'url': xml_get(story, 'url'),
                'owner': xml_get(story, 'owned_by').replace(' ', '&nbsp;'),
                'state': 'started',
            })
        qs = {
            'filter': 'state:unstarted',
        }
        xml = pv.projects(id).stories(**qs).get_etree()
        for story in xml.getchildren():
            data[proj_name].append({
                'name': xml_get(story, 'name'),
                'url': xml_get(story, 'url'),
                'owner': xml_get(story, 'owned_by').replace(' ', '&nbsp;'),
                'state': 'unstarted',
            })

    template = Template('''
        <html><body>
        <table border="0" cellpadding="4" cellspacing="0">
        {% for proj, stories in data.iteritems %}
            {% if stories %}
                <tr bgcolor="#e0ebff"><td colspan="3"><strong>{{ proj }}</strong></td></tr>
                <tr bgcolor="#e0ebff">
                    <th align="left">Task URL</th>
                    <th align="left">Assigned</th>
                    <th align="left">State</th>
                </tr>
                {% for story in stories %}
                    <tr bgcolor="{% cycle "#eeeeee" "#ffffff" %}">
                    <td valign="top"><a href="{{ story.url }}" style="text-decoration:none;">{{ story.name }}</a></td>
                    <td valign="top">{{ story.owner|default:"unassigned"|safe }}</td>
                    <td valign="top">{{ story.state }}</td>
                    </tr>
                {% endfor %}
            {% endif %}
        {% endfor %}
        </table>
        </body></html>
    ''')
    html = template.render(Context({'data':data}))

    # Email
    subject = 'Pivotal Tracker Report for %s' % (datetime.datetime.strftime(
        datetime.datetime.now(), '%b %d %Y'))
    from_email = 'Pivotal Reports <email@example.com>'
    to = person['email']
    text_content = 'Pivotal Tracker report...'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html, "text/html")
    msg.send()

