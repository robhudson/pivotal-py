from setuptools import setup


long_description = open('README.rst').read() + open('CHANGES.rst').read()

setup(
    name='pivotal-py',
    version=__import__('pivotal').__version__,
    description='Thin client for Pivotal Tracker\'s API',
    long_description=long_description,
    author='Rob Hudson',
    author_email='rob@cogit8.org',
    url='http://github.com/robhudson/pivotal-py/',
    packages=['pivotal'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
)

