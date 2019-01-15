import boto3
from moto import mock_s3
import botocore
import unittest

def upload_testing_file():
	return 3

class TestImageDownloader(unittest.TestCase):
    
    @mock_s3
    def setUp(self):
        client = boto3.client('s3')
    	conn = boto3.resource('s3', region_name='us-east-1')
    	# We need to create the bucket since this is all in Moto's 'virtual' AWS account
    	conn.create_bucket(Bucket='somenewbuckettotests3')

    @mock_s3
    def test_bucket_name(self):
    	client = boto3.client('s3')
    	buckets = [bucket['Name'] for bucket in response['Buckets']]
        self.assertEqual(buckets[0], 'somenewbuckettotests3')

if __name__ == '__main__':
    unittest.main()