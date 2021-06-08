Braze Python SDK
================

SDK for Braze API: https://www.braze.com/docs/api/basics/


Requirements
------------

* >=Python 3.7.5

Installation
------------
```
    pip install braze_sdk
```

Goal
----

To provide a python API client for Braze API.
(More clients to be implemented)

Code sample
-----------

Adding custom attributes for external_ids.
(Dataframe has the following schema):
```
external_id, custom_attribute1, custom_attribute2.........
```

```python

  import pandas as pd
  df = pd.read_csv('test.csv')
  u = UserDataClient(api_key='xxxxxxxxxxxxxx')
  res = u.users_track(df)
  res.text
```

Result from response type: forecast and forecastHourly
```python
    '{"attributes_processed":3,"message":"success"}'

```

Contributors
------------

* Paulo Kuong ([@pkuong](https://github.com/paulokuong))
