Kevin
- Unknown changes needed to support Django 2.0
- Creation of Pipfile, deletion of requirements.txt

Maddie
- Copy get_intraday_data task to fitapp/tasks.py
- Add documentation for get_intraday_data
- Refactor get_intraday_data to be clearer and more readable


Guide to changes

`tasks.get_intraday_data` is a helper function which provides support for retrieving intraday data
using `tasks.get_time_series_data`.