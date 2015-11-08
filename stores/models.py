from . import abstract_models
from django.apps import apps

#
# Copy from django-oscar project 
# from oscar.core.loading import is_model_registered
#
def is_model_registered(app_label, model_name):
    """
    Checks whether a given model is registered. This is used to only
    register Oscar models if they aren't overridden by a forked app.
    """
    try:
        apps.get_registered_model(app_label, model_name)
    except LookupError:
        return False
    else:
        return True

__all__ = []

if not is_model_registered('stores', 'StoreAddress'):
    class StoreAddress(abstract_models.AbstractStoreAddress):
        pass
    __all__.append('StoreAddress')


if not is_model_registered('stores', 'StoreGroup'):
    class StoreGroup(abstract_models.AbstractStoreGroup):
        pass
    __all__.append('StoreGroup')


if not is_model_registered('stores', 'Store'):
    class Store(abstract_models.AbstractStore):
        pass
    __all__.append('Store')


if not is_model_registered('stores', 'OpeningPeriod'):
    class OpeningPeriod(abstract_models.AbstractOpeningPeriod):
        pass
    __all__.append('OpeningPeriod')


if not is_model_registered('stores', 'StoreStock'):
    class StoreStock(abstract_models.AbstractStoreStock):
        pass
    __all__.append('StoreStock')

