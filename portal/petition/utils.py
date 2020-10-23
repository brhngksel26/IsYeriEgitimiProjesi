from __future__ import unicode_literals

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from passporteye import read_mrz

from xhtml2pdf import pisa

import os
from django.conf import settings
from django.test.signals import setting_changed

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None




PDF_GENERATOR_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULTS = {
    'UPLOAD_TO': 'pdfs',
    'PHANTOMJS_BIN_PATH': 'phantomjs',
    'DEFAULT_RASTERIZE_SCRIPT': os.path.join(PDF_GENERATOR_DIR, 'rasterize.js'),
    'DEFAULT_TEMP_DIR': os.path.join(PDF_GENERATOR_DIR, 'temp'),
    'TEMPLATES_DIR': os.path.join(PDF_GENERATOR_DIR, 'templates/pdf_generator')
}


class PDFSettings(object):
    """
    A settings object, that allows PDF settings to be accessed as properties.
    For example:
        from pdf_generator.settings import api_settings
        print(pdf_settings.UPLOAD_TO)
    """
    def __init__(self, user_settings=None, defaults=None):
        if user_settings:
            self._user_settings = user_settings
        self.defaults = defaults or DEFAULTS

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'PDF_GENERATOR', {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid PDF Generator setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Cache the result
        setattr(self, attr, val)
        return val


pdf_settings = PDFSettings(None, DEFAULTS)


def reload_pdf_settings(*args, **kwargs):
    global pdf_settings
    setting, value = kwargs['setting'], kwargs['value']
    if setting == 'PDF_GENERATOR':
        pdf_settings = PDFSettings(value, DEFAULTS)


setting_changed.connect(reload_pdf_settings)


def test(*args, **kwargs):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'baz.txt')