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

def update_country_in_dynamo(name,value):
    """update a country in the table with the key name and value"""
    table = get_table()
    # update_item arguments troubleshot with chat gpt
    response = table.update_item(
    Key={'Name': name},
        UpdateExpression="SET #pd = :val",
        ExpressionAttributeNames={
            "#pd": "Popeulation Density" # Alias needed because of the space in attribute name
        },
        ExpressionAttributeValues={
            ":val": value
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
