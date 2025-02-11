import time
from fastapi import Request
from . import LOG


async def middleware_log(request: Request, call_next):
    start = time.time()
    response = await call_next(request)

    if (request.url.path == '/metrics'): 
        return response

    try:
        status_code = response.status_code
    except Exception:
        status_code = 0

    total = round((time.time() - start), 4)
    log_dict = {
        "status_code":  status_code,
        "url":          request.url.path,
        "method":       request.method,
        "time":         f"{total} sec",
        "pathParams":   request.path_params,
        "queryParams":  dict(request.query_params),
        "client":       request.client.host, # type: ignore
        "host":         request.headers.get("host")
    }
    LOG.debug(log_dict)

    return response
