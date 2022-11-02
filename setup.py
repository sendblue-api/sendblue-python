from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'A tiny client wrapper for the Sendblue API in Python'
LONG_DESCRIPTION = 'Sendblue is a simple and powerful iMessage API. This is a tiny client wrapper for the Sendblue API in Python. With it we can send iMessages, SMS, and MMS, directly from Python.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="sendblue", 
        version=VERSION,
        author="Nikita Jerschow",
        author_email="nikita@sendblue.co",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["requests"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
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