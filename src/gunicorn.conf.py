import multiprocessing

bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
# This allows gunicorn to use an ASGI server that's compatible with FastAPI
worker_class = "uvicorn.workers.UvicornWorker"
