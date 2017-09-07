from setuptools import setup, find_packages

setup(
    name='ConfLoad',
    version='1.0.2',
    description='Configuration file loader and parser',
    long_description=open('README.md').read(),
    author='Newcraft',
    author_email='cedric.le.varlet@newcraftgroup.com',
    url='https://github.com/conversioncompany/nci-config-loader',
    download_url='https://github.com/conversioncompany/nci-config-loader/tarball/master',
    packages=find_packages(),
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3'
                 ],
)
