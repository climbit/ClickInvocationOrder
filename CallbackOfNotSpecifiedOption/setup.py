from setuptools import setup

setup(
    name='CallbackOfNotSpecifiedOption',
    version='1.0',
    py_modules=['cli'],
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        clickCallbackOfNotSpecifiedOption=cli:new
    ''',
)