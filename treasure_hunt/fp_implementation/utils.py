import functools


def list_output_to_str(func):
    @functools.wraps(func)
    def wrapper_list_output_to_str(*args, **kwargs):
        list_output = func(*args, **kwargs)
        return ' '.join(map(str, list_output))

    return wrapper_list_output_to_str
