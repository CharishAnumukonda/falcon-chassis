import falcon
from wsgiref import simple_server
# from app.middlewares.db_session_manager import SessionManager
# from config.db_client import Session

# session = Session()

api = falcon.API(middleware=[
    # SessionManager(session),
])


# ADD URLS HERE


if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()
