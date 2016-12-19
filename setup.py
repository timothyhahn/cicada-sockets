from setuptools import find_packages, setup

dependencies = [
    'tornado==4.4.2',
    'websocket-client==0.40.0'
]

setup(
    name='cicada-sockets',
    version='0.1.0',
    url='https://github.com/timothyhahn/cicada-sockets',
    author='Tim Hahn',
    author_email='timyhahn@gmail.com',
    description='Tornado handler for websocket connections',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
