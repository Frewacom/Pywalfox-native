import os
import logging

from utils.colors import generate_brighter_shade

def get_colorscheme(path, shade_modifier):
    """
    Fetches the pywal colors from the cache file.

    :param path str: the path to file that contains the pywal colors
    :return: the colors generated by pywal
    :rType: list
    """
    colors = []
    try:
        with open(os.path.expanduser(path), 'r') as f:
            for line in f.readlines():
                colors.append(line.rstrip('\n'))
    except IOError:
        error_message = 'Could not read colors from: %s' % path
        logging.error(error_message)
        return (False, error_message)

    if len(colors) < 16:
        error_message = '%s containing the generated pywal colors is invalid' % path
        logging.error(error_message)
        return (False, error_message)

    colors.append('#ffffff')
    colors.append(generate_brighter_shade(colors[0], shade_modifier))

    logging.debug('Successfully fetched pywal colors and created colorscheme')
    return (True, colors)

