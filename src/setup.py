from setuptools import setup, find_packages

setup(
    name='simplelayout-baokairui',
    packages=find_packages(where='src'),
    install_requires=['numpy',
                      'matplotlib',
                      'scipy'
                      ],
    entry_points={
        'console_scripts': [
            'simplelayout=simplelayout.__main__:main',
        ]},
)
