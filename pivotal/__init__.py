from pivotal import Pivotal

try:
    VERSION = __import__('pkg_resources').get_distribution('pivotal-py').version
except Exception, e:
    VERSION = 'unknown'
