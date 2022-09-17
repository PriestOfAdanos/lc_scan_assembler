from setuptools import setup

package_name = 'lc_scan_builder'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='phabrzyk',
    maintainer_email='pawelhabrzyk@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lc_scan_builder_node = lc_scan_builder.lc_scan_builder_node:main'
        ],
    },
)
