from setuptools import setup
import codecs

setup(
    name='instagram_uploader',
    version='0.1',
    py_modules=['instagram_uploader'],
    install_requires=[
        'click'
    ],
    dependency_links = [
        'https://github.com/Julioocz/Instagram-API-python'
    ],
    entry_points='''
        [console_scripts]
        instagram_uploader=instagram_uploader:instagram_upload
    ''',
)