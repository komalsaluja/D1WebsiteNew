from django_hosts import patterns, host


host_patterns = patterns('',
    host(r'www', 'frontend.urls', name='www'),
    host(r'adminpanel', 'api.urls', name='adminpanel'),
)
