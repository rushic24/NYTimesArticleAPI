===========
NYTimesArticleAPI
===========

``NYTimesArticleAPI`` is a fully-functional Python wrapper for the `New York Times Article Search API <https://developer.nytimes.com/article_search_v2.json>`_. 


Installation
=========

With pip::

    $ pip install NYTimesArticleAPI


Dependencies
=========

NYTimesArticleAPI requires the `requests <https://pypi.python.org/pypi/requests>`_ package.


Usage
=========

Simply import and initialize the API with your developer key::

    >>> from NYTimesArticleAPI import articleAPI
    >>> api = articleAPI('*YourAPIKey*')

Then call the ``search`` function with your desired search parameters/values::

    >>> articles = api.search(q='Obama', 
                              fq={'headline': 'Obama', 'source': ['Reuters', 'AP', 'The New York Times']}, 
                              begin_date="20111231", 
                              facet_field=['source', 'day_of_week'], 
                              facet_filter=True)

The search function returns a dictionary of the search results.

You can specify multiple filters by using a dictionary::
    >>> fq = {'headline': 'Obama', 'source': ['Reuters', 'AP', 'The New York Times']}

And multiple values by using a list::
    >>> facet_field = ['source', 'day_of_week']

More examples::

    >>> articles = api.search(q='Obama')

    >>> articles = api.search(q='Obama', begin_date="20111231", page=2)


For a complete overview of the available search parameters, please refer to the NYTimes Article Search API `Documentation <http://developer.nytimes.com/docs/read/article_search_api_v2>`_.

History
=========

This package was originally written by `Evan Sherlock <https://github.com/evansherlock>`_ as `nytimesarticle <https://github.com/evansherlock/nytimesarticle>`_. It has since been forked and updated by `Matt Morrison <https://github.com/MattDMo>`_, and subsequently released as `NyTimesArticleAPI <https://pypi.python.org/pypi/NYTimesArticleAPI>`_, with contributions from `Gerald Spencer <https://github.com/Geethree>`_ and `Andrew Han <https://github.com/handrew>`_.
