import os

from botocore.exceptions import ClientError
from flask import jsonify,Blueprint
import logging
from dotenv import load_dotenv
import boto3

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

routes = Blueprint('api', __name__)

def get_dynamodb_attribute(table_name, key_name, key_value):
    """
    Retrieves a specific attribute from a DynamoDB table using the given key.

    :param table_name: Name of the DynamoDB table.
    :param key_name: Name of the partition key (e.g., 'codeName').
    :param key_value: Value of the partition key.
    :param attribute_name: Name of the attribute to retrieve from the item.
    :return: The value of the attribute if found, 'NOT_FOUND' if the attribute is missing, or 404 if the item does not exist.
    """
    session = init_aws_session()
    dynamodb = session.resource('dynamodb')

    logger.info(f"Retrieving from table '{table_name}' where {key_name} = '{key_value}'")

    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(Key={key_name: key_value})
        return response
    except ClientError as e:
        if e.response['Error']['Code'] == 'UnrecognizedClientException':
            logger.error("Invalid AWS credentials or security token.")
            return {"error": "Invalid AWS credentials or security token"}
        else:
            logger.error(f"ClientError: {e}")
            return {"error": str(e)}
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {"error": f"Unexpected error: {str(e)}"}


def init_aws_session():
    """
    Initializes the AWS session with credentials from environment variables.
    :return: boto3 session object
    """
    logger.info("Initializing AWS session with credentials from environment variables.")
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv('AWS_REGION')
    )

    return session


def get_secret_code(code_name):
    """
    Retrieves the secret code from DynamoDB for the given code name.
    :param code_name:
    :return: the secret code associated with the code name, or 'NOT_FOUND' if it does not exist.
    """
    dynamodb_attribute = get_dynamodb_attribute(
        table_name=os.getenv('DYNAMODB_TABLE_NAME', "devops-challenge"),
        key_name='codeName',
        key_value=code_name
    )

    if 'Item' in dynamodb_attribute:
        return dynamodb_attribute['Item'].get('secretCode', 'NOT_FOUND')
    else:
        logger.error(
            f"Item with codeName '{code_name}' not found in DynamoDB table '{os.getenv('DYNAMODB_TABLE_NAME')}'.")
        return 404

@routes.route('/secret')
def extract_secret():
    logger.info(f"Route '/secret' get the secret code for codeName = {os.getenv('CODE_NAME')}")
    secret_code = get_secret_code(os.getenv('CODE_NAME'))
    if secret_code == 404:
        return jsonify({"error": "Secret code not found"}), 404
    return jsonify({
        "secret_code": secret_code
    })

@routes.route('/health')
def health_check():
    logger.info("Route '/health' accessed, performing health check.")
    return jsonify({
        "status": "healthy",
        "container": os.getenv("LINK_TO_DOCKER_HUB", "Not provided"),
        "project": os.getenv("GITHUB_PROJECT", "Not provided")
    })


@routes.route('/')
def default_route():
    logger.info("Route '/' accessed, this is the default route.")
    return "Welcome to my secret code service!"