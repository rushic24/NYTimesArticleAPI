from distutils.core import setup
import NYTimesArticleAPI as nytapi

setup(
    name='NYTimesArticleAPI',
    version=nytapi.__version__,
    author='Matt Morrison',
    author_email='mattdmo@pigimal.com',
    py_modules=['NYTimesArticleAPI'],
    url='https://github.com/MattDMo/NYTimesArticleAPI',
    license='LICENSE',
    description='Python wrapper for the New York Times Article Search API',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests >= 2.1.0",
    ],
)

