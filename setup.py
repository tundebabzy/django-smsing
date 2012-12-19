from setuptools import setup, find_packages

version = __import__('smsing').__version__

setup(
    name="django-smsing",
    version=version,
    url='http://github.com/tundebabzy/django-smsing',
    license='BSD',
    platforms=['OS Independent'],
    description="A simple API to send SMS messages.",
    author='Babatunde Akinyanmi',
    author_email='tundebabzy@gmail.com',
    maintainer='Babatunde Akinyanmi',
    maintainer_email='tundebabzy@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
