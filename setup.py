from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gol',
    version='0.0.1',
    description='Experiments with probabilistic kernel-based games of life.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/abelriboulot/gol',
    author='Abel Riboulot',
    author_email='abel@kta.io',
    package_dir={'': 'gol'},
    packages=find_packages(where='gol'),  # Required
    python_requires='>=3.5, <4',
    install_requires=[],
    extras_require={
        'dev': [],
        'test': [],
    },

    package_data={
        'sample': [],
    },

    entry_points={
        # 'console_scripts': [
        #     'sample=sample:main',
        # ],
    },

    project_urls={
        'Repo': 'https://github.com/abelriboulot/gol',
    },
)