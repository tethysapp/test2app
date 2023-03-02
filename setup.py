from setuptools import setup, find_namespace_packages
from setup_helper import find_all_resource_files


# -- Apps Definition -- #


namespace = 'tethysapp'
app_package = 'test2app'
release_package = f'{namespace}-{app_package}'


# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_all_resource_files(app_package, namespace)



setup(
    name=release_package,
    version='0.0.16',
    description='',
    long_description='',
    keywords='',
    author='',
    author_email='',
    url='https://github.com/romer8/test2app',
    license='',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)