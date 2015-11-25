from django.http import HttpResponse

'''
<WSGIRequest
path:/,
GET:<QueryDict: {u'a': [u'1'], u'b': [u'2']}>,
POST:<QueryDict: {}>,
COOKIES:{'csrftoken': 'Wf9T3cHYQc6kZz40gSc25OyCtGNOUwZU'},
META:{'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.GUBb7dSa8D/Render',
 'COLORFGBG': '12;8',
 'CONTENT_LENGTH': '',
 'CONTENT_TYPE': 'text/plain',
 u'CSRF_COOKIE': u'Wf9T3cHYQc6kZz40gSc25OyCtGNOUwZU',
 'DISPLAY': '/private/tmp/com.apple.launchd.ocNOxN1NKn/org.macosforge.xquartz:0',
 'DJANGO_SETTINGS_MODULE': 'engine.settings',
 'GATEWAY_INTERFACE': 'CGI/1.1',
 'HOME': '/Users/abhishektiwari',
 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, sdch',
 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.8,hi;q=0.6,ru;q=0.4',
 'HTTP_CACHE_CONTROL': 'max-age=0',
 'HTTP_CONNECTION': 'keep-alive',
 'HTTP_COOKIE': 'csrftoken=Wf9T3cHYQc6kZz40gSc25OyCtGNOUwZU',
 'HTTP_HOST': 'localhost:8000',
 'HTTP_UPGRADE_INSECURE_REQUESTS': '1',
 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
 'ITERM_PROFILE': 'Default',
 'ITERM_SESSION_ID': 'w0t0p0',
 'LANG': 'en_US.UTF-8',
 'LOGNAME': 'abhishektiwari',
 'OLDPWD': '/Users/abhishektiwari/work/engine',
 'PATH': '/opt/local/bin:/opt/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/usr/local/mysql/bin:/usr/local/Cellar/mysql/:/usr/local/Cellar/mysql/5.6.26/:/usr/local/Cellar/mysql/5.6.26/bin/:/usr/local/mysql/bin',
 'PATH_INFO': u'/',
 'PWD': '/Users/abhishektiwari/work/apigee',
 'QUERY_STRING': 'a=1&b=2',
 'REMOTE_ADDR': '127.0.0.1',
 'REMOTE_HOST': '',
 'REQUEST_METHOD': 'GET',
 'RUN_MAIN': 'true',
 'SCRIPT_NAME': u'',
 'SERVER_NAME': '12.10.10.10.in-addr.arpa',
 'SERVER_PORT': '8000',
 'SERVER_PROTOCOL': 'HTTP/1.1',
 'SERVER_SOFTWARE': 'WSGIServer/0.1 Python/2.7.10',
 'SHELL': '/bin/bash',
 'SHLVL': '1',
 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.WkgpzdWN41/Listeners',
 'TERM': 'xterm-256color',
 'TERM_PROGRAM': 'iTerm.app',
 'TMPDIR': '/var/folders/9s/p58qk2dd2vdgfrjwjk4s3zc00000gn/T/',
 'TZ': 'UTC',
 'USER': 'abhishektiwari',
 'VERSIONER_PYTHON_PREFER_32_BIT': 'no',
 'VERSIONER_PYTHON_VERSION': '2.7',
 'XPC_FLAGS': '0x0',
 'XPC_SERVICE_NAME': '0',
 '_': '/usr/bin/python',
 '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0',
 'wsgi.errors': <open file '<stderr>', mode 'w' at 0x105cf51e0>,
 'wsgi.file_wrapper': <class wsgiref.util.FileWrapper at 0x106bf6db8>,
 'wsgi.input': <socket._fileobject object at 0x108222250>,
 'wsgi.multiprocess': False,
 'wsgi.multithread': True,
 'wsgi.run_once': False,
 'wsgi.url_scheme': 'http',
 'wsgi.version': (1, 0)}>
'''


def default(request):
    print request.path
    return HttpResponse("<pre>Hello {0} /default.".format(request.path))

def add_user(request):
    return HttpResponse("<pre>200 OK {0} /user".format(request.method))

def add_to_auction(request):
    return HttpResponse("<pre>200 OK {0} /auction".format(request.method))

def get_bids(request):
    return HttpResponse("<pre>200 OK {0} /bid".format(request.method))

def add_item(request):
    return HttpResponse("<pre>200 OK {0} /item".format(request.method))
