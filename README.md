# query_athena
---
This is a Python package which includes reusable functions where you can import and use within your project files. This script executes query in athena and saves the result in the given s3 path.

## Installation

Using the package manager(pip), you can install this package from the git as shown below.  
Run this command in your home directory for installation.

``` 
pip install git+https://github.com/affinityanswers/query-athena.git
```

## Usage

You can import the package and functions to verify if it is installed properly.

```python 
from query_athena import query_athena
```

Use the below command for usage of function, its positional and optional arguments.

```python 
query_athena --help
usage: query_athena.py [-h] [--delete [DELETE]] [--delete_meta [DELETE_META]] [--workgroup WORKGROUP] [--region REGION] query s3_path

This script executes query in athena and saves the result in the given s3 path

positional arguments:
  query                 Query to be executed in athena
  s3_path               S3 path where athena query results will be saved

options:
  -h, --help            show this help message and exit
  --delete [DELETE]     If passed then existing path will be cleared before starting the query
  --delete_meta [DELETE_META]
                        Delete the metadata file after query is executed
  --workgroup WORKGROUP
                        Workgroup to use for the query
  --region REGION       Region we are running the AWS Athena query on
```

## Example

```python
from query_athena import query_athena
  
sql = "SELECT * FROM table limit 10"
staging_path = "s3://bucket/.../"
status = query_athena(sql, staging_path, False, False, workgroup="primary", region="us-west-2")
```
