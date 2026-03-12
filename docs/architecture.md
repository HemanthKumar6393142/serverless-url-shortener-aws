# Serverless URL Shortener Architecture

User → S3 Static Website → API Gateway → Lambda → DynamoDB

Redirect Flow:
User → Short URL → API Gateway → Lambda → DynamoDB → Redirect

Analytics Flow:
User → API Gateway → Lambda → DynamoDB → Response