from setuptools import setup

classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
packages = [
    "nextcord.ext.activities",
]
setup(
    name='nextcord-ext-activities',
    version='2022.02.25.post1',
    description='An nextcord extension that helps you to launch activities on Discord.',  # noqa: E501
    long_description=open('README.md').read(),
    url='',
    author='MaskDuck',
    license='MIT',
    classifiers=classifiers,
    keywords='activities',
    packages=packages,
    long_description_content_type='text/markdown',
    install_requires=['nextcord']
)
