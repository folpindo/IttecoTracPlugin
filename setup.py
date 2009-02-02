try:
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    pass #Is installing from a source package is not copied locally
from setuptools import setup, find_packages

from itteco import __package__, __version__

setup(
    name=__package__,
    version=__version__,
    author='Itteco.com',
    url='http://www.itteco.com/',
    description='Itteco Trac Plugin.',
    license='Apache License 2.0',
    packages=find_packages(),
    package_data={'itteco': ['templates/*', 'htdocs/images/*', 'htdocs/css/*', 'htdocs/js/jquery.ui/*','htdocs/js/*.js'],
                  'itteco.config': ["*.ini"]},
    entry_points = {'trac.plugins': ['itteco.init = itteco.init',
                                     'itteco.scrum.web_ui = itteco.scrum.web_ui',
                                     'itteco.ticket.admin = itteco.ticket.admin',
                                     'itteco.ticket.roadmap = itteco.ticket.roadmap',
                                     'itteco.ticket.web_ui = itteco.ticket.web_ui']},
    install_requires=['trac >= 0.11'], 
)