
# Create your tests here.
from django.test import TestCase

from imagenes.models import Imagen

class ImgModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Imagen.objects.create(titulo='Big', fecha_subida='07/12/2021')
        