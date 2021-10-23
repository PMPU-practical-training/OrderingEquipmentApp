import logging


from server import endponts
from server.exceptions import exceptions as server_exceptions
from database.lib.handler import DBHandler


logger = logging.getLogger(__name__)


ENDPOINT_NAME_TO_REQUEST_PROCESSOR = {
    'get_user': endponts.get_user,
}


def process_request(endpoint_name, data):
    logger.info('Request to {}: {}'.format(endpoint_name, data))

    endpoint_processor = ENDPOINT_NAME_TO_REQUEST_PROCESSOR.get(endpoint_name)
    if not endpoint_processor:
        raise server_exceptions.EndpointNotFountError(endpoint_name)

    with DBHandler() as handler:
        return endpoint_processor(handler, data)
