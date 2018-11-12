from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
     name='terminal-text',    
     version='1.1',                         
     scripts=['termtext'],
     description='Its a simple commandline tool that allows you send text messages and mms to your phone using terminal',
     install_requires=[
        "docopt",
    ],
    classifiers=[
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Programming Language :: Python',
    		'Programming Language :: Python :: 3.6'
   ],
    long_description=long_description,
    long_description_content_type='text/markdown'
 )
