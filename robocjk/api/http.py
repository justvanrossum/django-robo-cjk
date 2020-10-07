# -*- coding: utf-8 -*-

from django.http import JsonResponse


class ApiResponse(JsonResponse):

    def __init__(self, data=None, status=None, error=None):
        super(ApiResponse, self).__init__(
            data={
                'data': data,
                'status': status,
                'error': error,
            },
            status=status,
            json_dumps_params={
                'sort_keys':True,
            })

    def _format_error(self, prefix, message=''):
        return '{} - {}'.format(prefix, message) if message else prefix


class ApiResponseSuccess(ApiResponse):

    def __init__(self, data):
        super(ApiResponseSuccess, self).__init__(
            data=data, status=200, error=None)


class ApiResponseError(ApiResponse):

    # 400 Bad Request - The server cannot or will not process the request due to an apparent client error (e.g., malformed request syntax, size too large, invalid request message framing, or deceptive request routing).
    # 401 Unauthorized - Similar to 403 Forbidden, but specifically for use when authentication is required and has failed or has not yet been provided
    # 403 Forbidden - The request contained valid data and was understood by the server, but the server is refusing action
    # 404 Not Found - The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible.
    # 405 Method Not Allowed - A request method is not supported for the requested resource

    def __init__(self, status, error):
        super(ApiResponseError, self).__init__(
            data=None, status=status, error=error)


class ApiResponseBadRequest(ApiResponseError):

    def __init__(self, error=''):
        super(ApiResponseBadRequest, self).__init__(
            status=400, error=self._format_error('Bad Request', error))


class ApiResponseUnauthorized(ApiResponseError):

    def __init__(self, error=''):
        super(ApiResponseUnauthorized, self).__init__(
            status=401, error=self._format_error('Unauthorized', error))


class ApiResponseForbidden(ApiResponseError):

    def __init__(self, error=''):
        super(ApiResponseForbidden, self).__init__(
            status=403, error=self._format_error('Forbidden', error))


class ApiResponseNotFound(ApiResponseError):

    def __init__(self, error=''):
        super(ApiResponseNotFound, self).__init__(
            status=404, error=self._format_error('Not Found', error))


class ApiResponseMethodNotAllowed(ApiResponseError):

    def __init__(self, error=''):
        super(ApiResponseMethodNotAllowed, self).__init__(
            status=405, error=self._format_error('Method Not Allowed', error))


class ApiResponseInternalServerError(ApiResponseError):

    def __init__(self, error=''):
        super(ApiResponseInternalServerError, self).__init__(
            status=500, error=self._format_error('Internal Server Error', error))
        # TODO: log
