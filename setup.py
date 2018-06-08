import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = ['requests']

version = ''
with open('betsapi/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='betsapi',
    packages=['betsapi'],
    version=version,
    description='betsapi python SDK',
    author='meoww',
    author_email='i@meoww.app',
    install_requires=requires,
    url='https://github.com/qwqmeow/betsapi-python',
    download_url='https://github.com/qwqmeow/betsapi-python/releases',
    keywords=['bet', 'api', 'odds'],
    classifiers=[],
)
