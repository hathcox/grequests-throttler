__title__ = 'RequestsThrottler'
__version__ = '0.1.0'
__author__ = 'Lou Marvin Caraig'
__author_email__ = 'loumarvincaraig@gmail.com'
__project_url__ = 'https://github.com/se7entyse7en/requests-throttler'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2013 Lou Marvin Caraig'


from . import utils
from .throttled_request.throttled_request import ThrottledRequest
from .throttler.base_throttler import BaseThrottler