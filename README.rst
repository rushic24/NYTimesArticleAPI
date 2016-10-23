NYTimesArticleAPI
=================

``NYTimesArticleAPI`` is a fully-functional Python wrapper for the `New
York Times Article Search
API <https://developer.nytimes.com/article_search_v2.json>`__.

Installation
------------

With pip:

::

    $ pip install NYTimesArticleAPI

Dependencies
------------

NYTimesArticleAPI requires the
```requests`` <https://pypi.python.org/pypi/requests>`__ and
```setuptools`` <https://pypi.python.org/pypi/setuptools>`__ packages.

Usage
-----

Simply import and initialize the API with your developer key:

.. code:: python

    >>> from NYTimesArticleAPI import articleAPI
    >>> api = articleAPI("YourAPIKey")

Then call the ``search`` function with your desired search
parameters/values:

.. code:: python

    >>> articles = api.search(q="Obama", 
                              fq={"headline": "Obama", 
                                  "source": ["Reuters", 
                                             "AP", 
                                             "The New York Times"]}, 
                              begin_date="20161023", # this can also be an int
                              facet_field=["source", "day_of_week"], 
                              facet_filter=True)

The search function returns a Python dictionary of the search results.

You can specify multiple filters by using a dictionary::

.. code:: python

    >>> fq = {"headline": "Obama", "source": ["Reuters", "AP", "The New York Times"]}

And multiple values by using a list::

.. code:: python

    >>> facet_field = ["source", "day_of_week"]

More examples:

.. code:: python

    >>> articles = api.search(q="Obama")

    >>> articles = api.search(q="Obama", begin_date="20111231", page=2)

For a complete overview of the available search parameters, please refer
to the `NYTimes Article Search API
Documentation <http://developer.nytimes.com/docs/read/article_search_api_v2>`__.

History
-------

This package was originally written by `Evan
Sherlock <https://github.com/evansherlock>`__ as
```nytimesarticle`` <https://github.com/evansherlock/nytimesarticle>`__.
It has since been forked and updated by `Matt
Morrison <https://github.com/MattDMo>`__, and subsequently released as
```NyTimesArticleAPI`` <https://pypi.python.org/pypi/NYTimesArticleAPI>`__,
with contributions from `Gerald Spencer <https://github.com/Geethree>`__
and `Andrew Han <https://github.com/handrew>`__.

License
-------

© 2016 Matt Morrison mattdmo@pigimal.com.

This is free software. It is licensed under the `MIT
License <http://opensource.org/licenses/MIT>`__. Feel free to use this
in your own work. However, if you modify and/or redistribute it, please
attribute me in some way, and distribute your work under this or a
similar license. A shout-out or a beer would be appreciated.
