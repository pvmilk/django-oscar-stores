import os


# Keep a setting for the path to the templates in case a project subclasses the
# models and still needs to use the templates
OSCAR_STORES_MAIN_TEMPLATE_DIR  = os.path.join(
    os.path.dirname(__file__),
    'templates')
