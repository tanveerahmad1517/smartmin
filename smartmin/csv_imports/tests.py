from django.test import TestCase

from .models import ImportTask, generate_file_path


class ImportTest(TestCase):
    def test_csv_import(self):
        pass

    def test_generate_file_path(self):
        self.assertEquals(generate_file_path(ImportTask(), 'allo.csv'), 'csv_imports/allo.csv')
        self.assertEquals(generate_file_path(ImportTask(), 'allo.xlsx'), 'csv_imports/allo.xlsx')
        self.assertEquals(generate_file_path(ImportTask(), 'allo.foo.bar'), 'csv_imports/allo.foo.bar')

        long_name = 'foo' * 100
        self.assertEquals(generate_file_path(ImportTask(), '%s.xls.csv' % long_name),
                          'csv_imports/%s.csv' % long_name[:96])

        self.assertEquals(generate_file_path(ImportTask(), '%s.abc.xlsx' % long_name),
                          'csv_imports/%s.xlsx' % long_name[:95])
