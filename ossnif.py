from os import name as OSname

if OSname == 'posix':
    path_slash = '/'
elif OSname == 'nt':
    path_slash = '\\'
