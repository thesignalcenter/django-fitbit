Kevin
- Unknown changes needed to support Django 2.0
- Creation of Pipfile, deletion of requirements.txt

Maddie
- Copy get_intraday_data task to fitapp/tasks.py
- Add documentation for get_intraday_data
- Refactor get_intraday_data to be clearer and more readable

- Copy changes to get_time_series_data to support retreival of intraday data
- Refactor get_time_series_data to be a bit clearer
- add get_fitbit_profile to fitapp.utils

- added fields to TimeSeriesDataType and TimeSeriesData
- changed 0002_initial_data migration to get it to not complain


Guide to changes

`tasks.get_intraday_data` is a helper function which provides support for retrieving intraday data
using `tasks.get_time_series_data`.


`FITAPP_GET_INTRADAY` must be set. If true, intraday data will be attempted to be retrieved


Notes
For some reason, `get_intraday_data` does NOT use the given `intraday_time_series` function provided by
python-fitbit. It still works though using `time_series` because currently, with the type of request being made to that endpoint,
Fitbit returns both regular step data and intraday data assuming the app is authorized to get intraday.

Issues
Assumes that the app is authorized for intraday data, does not check this as far as I have seen