from bottle import abort


def get_object(model, instance_id, validation_callback=None, error_callback=None):

    if validation_callback is None:
        validation_callback = lambda obj: True

    if error_callback is None:
        error_callback = lambda: None

    if instance_id is None:
        return error_callback()

    elif isinstance(instance_id, basestring):
        try:
            instance_id = int(instance_id)
        except (TypeError, ValueError):
            return error_callback()

    try:
        instance = model.get_by_id(instance_id)
    except Exception:
        instance = None

    if instance is None:
        return error_callback()

    if not validation_callback(instance):
        return error_callback()

    return instance


def get_object_or_404(model, instance_id, validation_callback=None):
    return get_object(model, instance_id, validation_callback, lambda: abort(404))


def get_object_or_default(model, instance_id, validation_callback=None, default_value=None):
    return get_object(model, instance_id, validation_callback, lambda: default_value)


get_object_or_none = get_object_or_default
