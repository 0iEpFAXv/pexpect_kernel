import base64
import imghdr
import os

#from IPython.

def _TEXT_SAVED_IMAGE(name):
    return "%s: saved image data to:" % (name,)

def image_setup_cmd(name):
    return """
    display () {
        TMPFILE=$(mktemp ${TMPDIR-/tmp}/%s.XXXXXXXXXX)
        cat > $TMPFILE
        echo "%s $TMPFILE" >&2
    }
    """ % (name, _TEXT_SAVED_IMAGE(name))

def display_data_for_image(filename):
    with open(filename, 'rb') as f:
        image = f.read()
    os.unlink(filename)

    image_type = imghdr.what(None, image)
    if image_type is None:
        raise ValueError("Not a valid image: %s" % image)

    image_data = base64.b64encode(image).decode('ascii')
    content = {
        'data': {
            'image/' + image_type: image_data
        },
        'metadata': {}
    }
    return content


def extract_image_filenames(name, output):
    output_lines = []
    image_filenames = []

    for line in output.split("\n"):
        if line.startswith(_TEXT_SAVED_IMAGE(name)):
            filename = line.rstrip().split(": ")[-1]
            image_filenames.append(filename)
        else:
            output_lines.append(line)

    output = "\n".join(output_lines)
    return image_filenames, output
