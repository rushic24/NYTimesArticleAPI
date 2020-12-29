# nytimesarticlev2

`nytimesarticlev2` is a Python wrapper for the [New York Times Article Search API][1]. Based on the excellent [`requests`][13] package, it provides full support for all of the API's search parameters, and also allows access to the request object itself for debugging purposes.
  

## Installation

With pip:

    $ pip install nytimesarticlev2


## Dependencies

nytimesarticlev2 requires the [`requests`][2] and [`setuptools`][3] packages.


## Usage

Simply import and initialize the API with your developer key:

```python
>>> from nytimesarticlev2 import articleAPI
>>> api = articleAPI("YourAPIKey")
```

Then call the `search` function with your desired search parameters/values:

```python
>>> articles = api.search(q="Obama", 
                          fq={"headline": "Obama", 
                              "source": ["Reuters", 
                                         "AP", 
                                         "The New York Times"]}, 
                          begin_date="20161001", # this can also be an int
                          facet_field=["source", "day_of_week"], 
                          facet_filter=True)
```

The search function returns a Python dictionary of the search results.

You can specify multiple filters by using a dictionary::

```python
>>> fq = {"headline": "Obama", "source": ["Reuters", "AP", "The New York Times"]}
>>> articles = api.search(q="Obama", fq=fq)
```

And multiple values by using a list::

```python
>>> facet_field = ["source", "day_of_week"]
>>> articles = api.search(q="Obama", facet_field=facet_field)
```

More examples:

```python
# simple search
>>> articles = api.search(q="Obama")
# search between specific dates
>>> articles = api.search(q="Obama", begin_date="20161001", end_date="20161020", page=2)
# access most recent request object
>>> headers = api.req.headers
```

For a complete overview of the available search parameters, please refer to the [NYTimes Article Search API Documentation][4].


## History

This package was originally written by [Evan Sherlock][5] as [`nytimesarticle`][6]. It has since been forked and updated by [Matt Morrison][7], and subsequently released as [`NyTimesArticleAPI`][8], with contributions from [Gerald Spencer][9] and [Andrew Han][10]. Which I further updated to nytimesarticlev2.


## License

&copy; 2016 Matt Morrison <mattdmo@pigimal.com>.

This is free software. It is licensed under the [MIT License][11]. Feel free to use this in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and distribute your work under this or a similar license. A shout-out or a beer would be appreciated.

You can support development of this project on [Gratipay][12].


  [1]: https://developer.nytimes.com/article_search_v2.json
  [2]: https://pypi.python.org/pypi/requests
  [3]: https://pypi.python.org/pypi/setuptools
  [4]: http://developer.nytimes.com/docs/read/article_search_api_v2
  [5]: https://github.com/evansherlock
  [6]: https://github.com/evansherlock/nytimesarticle
  [7]: https://github.com/MattDMo
  [8]: https://pypi.python.org/pypi/nytimesarticlev2
  [9]: https://github.com/Geethree
  [10]: https://github.com/handrew
  [11]: http://opensource.org/licenses/MIT
  [12]: https://www.gratipay.com/on/github/MattDMo/
  [13]: http://docs.python-requests.org
