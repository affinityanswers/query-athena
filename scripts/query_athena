#!/usr/bin/env python3
import sys
import os
from argparse import ArgumentParser
from pyathena import connect
from subprocess import check_output, CalledProcessError
from traceback import format_exc


def query_athena(query, s3_path, delete, delete_meta, workgroup='primary', region='us-west-2'):
    """
    Execute the Query in Athena and save the results to S3 Path
    Args:
        query: The query to be executed in Athena
        s3_path: The path where the results will be saved
        delete: It is a boolean, If set to true exisitng content in the S3 path will be deleted before executing the path.
        delete_meta: It is a boolean, If set to true meta data will be deleted after query is executed
        workgroup: It is a string, points to AWS Athena workgroup to use for query.
        region: It is a string, the aws region to use for running the AWS Athena Query
    Returns:
        A tuple of query_id,output_location, data_scanned if query executed successfully False otherwise.
    """
    if delete:
       sys.stderr.write("Deleting all files in %s path\n"%(s3_path,))
       try:
          output = check_output(["aws", "--region", region, "s3", "rm", "--recursive", s3_path])
       except CalledProcessError as e:
          return False
    if workgroup == 'primary' and 'ATHENA_WORKGROUP' in os.environ:
       workgroup = os.environ['ATHENA_WORKGROUP']
    cursor = connect(s3_staging_dir=s3_path,
                 region_name=region, work_group=workgroup).cursor()
    try:
       cursor.execute(query)
    except:
       sys.stderr.write("Got following exception while querying athena\n%s\n"%(format_exc(),))
       return False
    data_scanned = cursor.data_scanned_in_bytes
    query_id = cursor.query_id
    output_location = cursor.output_location
    if delete_meta:
       try:
          output = check_output(["aws", "s3", "rm", "%s.metadata"%(output_location,)]) 
       except CalledProcessError as e:
          sys.stderr.write("Failed to delete metadata from s3")
    cursor.close()
    return query_id, output_location, data_scanned
    

def main():
    parser = ArgumentParser(description="This script executes query in athena and saves the result in the given s3 path")
    parser.add_argument("query", type=str, help="Query to be executed in athena")
    parser.add_argument("s3_path", type=str, help="S3 path where athena query results will be saved")
    parser.add_argument("--delete", type=str, nargs="?", const=True, default=False, help="If passed then existing path will be cleared before starting the query")
    parser.add_argument("--delete_meta", type=str, nargs="?", const=True, default=False, help="Delete the metadata file after query is executed")
    parser.add_argument("--workgroup", type=str, default="primary", help="Workgroup to use for the query")
    parser.add_argument("--region", type=str, default='us-west-2', help="Region we are running the AWS Athena query on")
    args = parser.parse_args()
    status = query_athena(args.query, args.s3_path, args.delete, args.delete_meta, args.workgroup, args.region)
    if status == False:
       sys.exit(2)
    else:
       query_id, output_location, data_scanned = status
       print(query_id)
       print(output_location)
       print(data_scanned)


if __name__ == "__main__":
   main()
