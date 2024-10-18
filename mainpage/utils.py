

def directory_path(instance, file_name):
    file = instance.__class__.__name__.lower()
    return f"media/{file}/{file_name}"