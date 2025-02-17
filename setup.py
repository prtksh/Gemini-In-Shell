from setuptools import setup, find_packages

setup(
    name='gemini-in-shell',  
    version='0.1.0',         
    packages=find_packages(),
    install_requires=[
        'google-generativeai',
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'shell-gemini=gemini_in_shell.gemini_run:main',  
        ],
    },
    description="CLI tool through which you can query the Gemini model",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Pratiksha Naik',
    author_email='naikprtksh@gmail.com',
    url='https://github.com/prtksh/Gemini-In-Shell',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

