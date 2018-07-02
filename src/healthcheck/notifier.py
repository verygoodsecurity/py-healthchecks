import logging
import os
import rollbar

rollbar.init(
    os.getenv('ROLLBAR_ACCESS_TOKEN'),
    environment=os.getenv('ROLLBAR_ENVIRONMENT', 'local'),
    allow_logging_basic_config=False
)


def alert(message, level='error'):
    rollbar.report_message(message, level)
