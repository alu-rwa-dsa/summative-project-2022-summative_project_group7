from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("CONTRIBUTORS.md", "r") as co:
    short_description = co.read()

setup(
    name='implementation',
    version='0.0.1',
    packages=['module',
              'Tests'],

    package_dir={'': 'implementation'},
    url='',
    license='',
    author=['Clare Kanja',
            'Leticia Darko',
            'Nicole Moyo',
            'Mukantwari Françoise',
            'John Mwangi'],

    author_email=['c.kanja@alustudent.com',
                  'l.darko@alustudent.com',
                  'n.moyo@alustudent.com',
                  'f.mukantwari@alustudent.com',
                  'j.mwangi@alustudent.com'],

    description='Sudoku Solver',

    long_description=[long_description, short_description],
    long_description_content_type="text/markdown",
)
