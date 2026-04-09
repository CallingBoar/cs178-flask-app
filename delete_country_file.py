# Bernardo Martinez

import boto3
from boto3.dynamodb.conditions import Key
from flask import render_template

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Countries"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def delete_country_from_dynamo(name):
    """deletes the item with key name from the table. Nothing happens if does not exist"""
    table = get_table()
    response = table.delete_item(Key = {"Name": name})
    return response
