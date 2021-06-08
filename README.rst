Braze Python SDK
--------------------

SDK for Braze API

    | SDK for Braze API.
    | https://www.braze.com/docs/api/basics/
    | https://github.com/paulokuong/braze

Requirements
------------

-  Python 3.7.0

Goal
----

| To provide a python API client for Braze API.
| (More clients to be implemented)

Code sample
-----------

| Adding custom attributes for external_ids.
| (Dataframe has the following schema):
| external_id, custom_attribute1, custom_attribute2.........

.. code:: python

  import pandas as pd
  df = pd.read_csv('test.csv')
  u = UserDataClient(api_key='xxxxxxxxxxxxxx')
  res = u.users_track(df)
  res.text


Contributors
------------

-  Paulo Kuong (`@paulokuong`)

.. @pkuong: https://github.com/paulokuong
