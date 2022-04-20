from waitress import serve
    
from ecommerce_website.wsgi import application
    
if __name__ == '__main__':
    serve(application, port='8000')