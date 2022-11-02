from setuptools import setup, find_packages

readme = open('README.md').read()

VERSION = '0.1.3' 
DESCRIPTION = 'A tiny client wrapper for the Sendblue API in Python'
LONG_DESCRIPTION = readme

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="sendblue", 
        version=VERSION,
        author="Nikita Jerschow",
        author_email="nikita@sendblue.co",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=["requests"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'

        repository="https://github.com/sendblue-api/sendblue-python",
        
        keywords=['imessage', 'api', 'sms', 'python', 'sendblue', 'sendblue python', 'sendblue api', 'imessage api', 'sms api'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)