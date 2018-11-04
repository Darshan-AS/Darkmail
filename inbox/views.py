from __future__ import print_function

from django.http import HttpResponse
from django.shortcuts import render

# inbox = Inbox()
messages = [{'id': '166de77315e49ab6', 'threadId': '166de77315e49ab6',
             'labelIds': ['UNREAD', 'IMPORTANT', 'CATEGORY_UPDATES', 'INBOX'],
             'snippet': '04 Nov, 2018 Hi Darshan Don Top companies like Cognizant, TCS, IBM, Infosys, HCL &amp; other IT Companies are hiring 10000 Candidates in Coming Next Month. Check out the jobs below &amp; apply ASAP.',
             'historyId': '557484', 'internalDate': '1541330640000', 'payload': {'mimeType': 'text/html', 'headers': [
        {'name': 'Date', 'value': '04 Nov 2018 16:54:00 +0530'},
        {'name': 'From', 'value': 'Interview Call Letter <jobs@techgig.com>'},
        {'name': 'To', 'value': 'darshandon.das465@gmail.com'}, {'name': 'Subject',
                                                                 'value': 'IBM India MEGA Hiring For Freshers As Software Developers - Apply And Get Hired Now'}]},
             'sizeEstimate': 77720}, {'id': '166de2a339de8503', 'threadId': '166dd5c7002c1a42',
                                      'labelIds': ['UNREAD', 'IMPORTANT', 'CATEGORY_PERSONAL', 'INBOX'],
                                      'snippet': '04 Nov, 2018 Hi Darshan AS Top companies like Cognizant, TCS, IBM, Infosys, HCL &amp; other IT Companies are hiring 10000 Candidates in Coming Next Month. Check out the jobs below &amp; apply ASAP. CPG',
                                      'historyId': '557565', 'internalDate': '1541325597000',
                                      'payload': {'mimeType': 'text/html',
                                                  'headers': [{'name': 'Date', 'value': '04 Nov 2018 15:29:57 +0530'},
                                                              {'name': 'From',
                                                               'value': 'Interview Call Letter <jobs@techgig.com>'},
                                                              {'name': 'To', 'value': 'itisdarshan@gmail.com'},
                                                              {'name': 'Subject',
                                                               'value': 'Gartner India MEGA Hiring For Freshers As Software Developers - Apply And Get Hired Now'}]},
                                      'sizeEstimate': 73905},
            {'id': '166dda93e82ef245', 'threadId': '166dda93e82ef245', 'labelIds': ['CATEGORY_SOCIAL', 'INBOX'],
             'snippet': 'Hi Darshan, I&#39;d like to join your LinkedIn network. LinkedIn Darshan AS Hi Darshan, I&#39;d like to join your LinkedIn network. Jakkidi Reddy Email Marketing Manager at movingDneedle Pvt. Ltd.',
             'historyId': '557189', 'internalDate': '1541317146000', 'payload': {'mimeType': 'multipart/alternative',
                                                                                 'headers': [{'name': 'From',
                                                                                              'value': 'Jakkidi Reddy <invitations@linkedin.com>'},
                                                                                             {'name': 'Subject',
                                                                                              'value': 'Darshan, please add me to your LinkedIn network'},
                                                                                             {'name': 'To',
                                                                                              'value': 'Darshan AS <itisdarshan@gmail.com>'},
                                                                                             {'name': 'Date',
                                                                                              'value': 'Sun, 4 Nov 2018 07:39:06 +0000 (UTC)'}]},
             'sizeEstimate': 32262},
            {'id': '166dd769203447f6', 'threadId': '166dd769203447f6', 'labelIds': ['CATEGORY_PROMOTIONS', 'INBOX'],
             'snippet': 'Daily Newsletter Sunday, 4th November 2018 Ban on H4 Visas could come into force next month Internet shutdowns: India tops the list with 121 incidents in 2018 Good news for Indian techies; hiring to',
             'historyId': '557372', 'internalDate': '1541313817000', 'payload': {'mimeType': 'text/html', 'headers': [
                {'name': 'Date', 'value': '04 Nov 2018 12:13:37 +0530'},
                {'name': 'From', 'value': 'TechGig Latest News <technews@techgig.com>'},
                {'name': 'To', 'value': 'itisdarshan@gmail.com'}, {'name': 'Subject',
                                                                   'value': 'Ban on H4 Visas could come into force next month | Internet shutdowns: India tops the list with 121 incidents in 2018'}]},
             'sizeEstimate': 20985}, {'id': '166dd5c7002c1a42', 'threadId': '166dd5c7002c1a42',
                                      'labelIds': ['UNREAD', 'IMPORTANT', 'CATEGORY_UPDATES', 'INBOX'],
                                      'snippet': '04 Nov, 2018 Hi Darshan Don Top companies like Cognizant, TCS, IBM, Infosys, HCL &amp; other IT Companies are hiring 10000 Candidates in Coming Next Month. Check out the jobs below &amp; apply ASAP.',
                                      'historyId': '557565', 'internalDate': '1541312110000',
                                      'payload': {'mimeType': 'text/html',
                                                  'headers': [{'name': 'Date', 'value': '04 Nov 2018 11:45:10 +0530'},
                                                              {'name': 'From',
                                                               'value': 'Interview Call Letter <jobs@techgig.com>'},
                                                              {'name': 'To', 'value': 'darshandon.das465@gmail.com'},
                                                              {'name': 'Subject',
                                                               'value': 'Gartner India MEGA Hiring For Freshers As Software Developers - Apply And Get Hired Now'}]},
                                      'sizeEstimate': 77920}, {'id': '166dc65676ebbb75', 'threadId': '166dc65676ebbb75',
                                                               'labelIds': ['UNREAD', 'CATEGORY_UPDATES', 'INBOX'],
                                                               'snippet': 'Reliance JIO Interview Questions TechGig Practice Platform Dear Darshan AS, When preparing for a job interview, it&#39;s not enough to just read advice you need to put that advice into practice! You',
                                                               'historyId': '556445', 'internalDate': '1541295881000',
                                                               'payload': {'mimeType': 'text/html', 'headers': [
                                                                   {'name': 'Date',
                                                                    'value': '04 Nov 2018 07:14:41 +0530'},
                                                                   {'name': 'From',
                                                                    'value': 'Interview Quiz <assessment@techgig.com>'},
                                                                   {'name': 'To', 'value': 'itisdarshan@gmail.com'},
                                                                   {'name': 'Subject',
                                                                    'value': 'Are You Ready To Solve 25 Famous Interview Quiz 2018-19'}]},
                                                               'sizeEstimate': 27854},
            {'id': '166dc2583d3c555a', 'threadId': '166dc2583d3c555a',
             'labelIds': ['UNREAD', 'IMPORTANT', 'CATEGORY_UPDATES', 'INBOX'],
             'snippet': '“This service is offered by TRANSFAST Remittance LLC (TF) through a direct contract with SBI India under Indian Law and regulation. SBI, New York has no connection to the arrangement; nor, is SBI, New',
             'historyId': '556311', 'internalDate': '1541291726000', 'payload': {'mimeType': 'text/html', 'headers': [
                {'name': 'Date', 'value': '04 Nov 2018 06:05:26 +0530'},
                {'name': 'From', 'value': 'team.sbi@sbi.co.in'}, {'name': 'To', 'value': 'darshandon.das465@gmail.com'},
                {'name': 'Subject', 'value': 'Remittances from USA now made easy!'}]}, 'sizeEstimate': 10544},
            {'id': '166db108cfddf8f9', 'threadId': '166db108cfddf8f9',
             'labelIds': ['UNREAD', 'CATEGORY_UPDATES', 'INBOX'],
             'snippet': 'Hey DarshanDon! A personal access token (git: https://github.com/ on DONS-WINDOWS at 04-Nov-2018 01:02) with gist and repo scopes was recently added to your account. Visit https://github.com/settings/',
             'historyId': '556167', 'internalDate': '1541273550000', 'payload': {'mimeType': 'text/plain', 'headers': [
                {'name': 'Date', 'value': 'Sat, 03 Nov 2018 19:32:30 +0000 (UTC)'},
                {'name': 'From', 'value': 'GitHub <noreply@github.com>'},
                {'name': 'To', 'value': 'Darshan Don <itisDarshan@gmail.com>'},
                {'name': 'Subject', 'value': '[GitHub] A personal access token has been added to your account'}]},
             'sizeEstimate': 5846}, {'id': '166dad1da3e88c23', 'threadId': '166dad1da3e88c23',
                                     'labelIds': ['UNREAD', 'CATEGORY_SOCIAL', 'INBOX'],
                                     'snippet': 'Hi Darshan, I&#39;d like to join your LinkedIn network. LinkedIn Darshan AS Hi Darshan, I&#39;d like to join your LinkedIn network. Mithun Mathew Senior Sales Executive at SAMS Solutions United Arab',
                                     'historyId': '557048', 'internalDate': '1541269474000',
                                     'payload': {'mimeType': 'multipart/alternative', 'headers': [
                                         {'name': 'From', 'value': 'Mithun Mathew <invitations@linkedin.com>'},
                                         {'name': 'Subject',
                                          'value': 'Darshan, please add me to your LinkedIn network'},
                                         {'name': 'To', 'value': 'Darshan AS <itisdarshan@gmail.com>'},
                                         {'name': 'Date', 'value': 'Sat, 3 Nov 2018 18:24:34 +0000 (UTC)'}]},
                                     'sizeEstimate': 32207}, {'id': '166dacd8f9f89411', 'threadId': '166dacd8f9f89411',
                                                              'labelIds': ['UNREAD', 'CATEGORY_PERSONAL', 'INBOX'],
                                                              'snippet': 'Google APIs Explorer connected to your Google Account Hi Darshan, Google APIs Explorer now has access to your Google Account itisdarshan@gmail.com. Google APIs Explorer can: Read, compose, send, and',
                                                              'historyId': '556256', 'internalDate': '1541269194000',
                                                              'payload': {'mimeType': 'multipart/alternative',
                                                                          'headers': [{'name': 'Date',
                                                                                       'value': 'Sat, 3 Nov 2018 18:19:54 +0000 (UTC)'},
                                                                                      {'name': 'Subject',
                                                                                       'value': 'Google APIs Explorer connected to your Google Account'},
                                                                                      {'name': 'From',
                                                                                       'value': 'Google <no-reply@accounts.google.com>'},
                                                                                      {'name': 'To',
                                                                                       'value': 'itisdarshan@gmail.com'}]},
                                                              'sizeEstimate': 13078}]


# Create your views here.s
def inbox(request):
    # messages = inbox.get_messages()
    return render(request, 'inbox/inbox.html', {'messages': messages})


def details(request, messageid):
    return HttpResponse('Works')
