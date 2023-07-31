# Function Deployment and Invocation Process

This diagram illustrates the process of deploying and invoking a cloud function involving the Developer, AWS Lambda, API Gateway, and S3 Bucket using ASCII art.


            +---------------------+
            |      Developer      |
            +---------------------+
                       |
                       |  Create cloud function
                       |
                       v
            +---------------------+
            |     AWS Lambda      |
            +---------------------+
                       |
                       |  Store code and
                       |  dependencies
                       v
            +---------------------+
            |      S3 Bucket      |
            +---------------------+
                       |
                       |  Create API endpoint
                       |
                       v
            +---------------------+
            |     API Gateway     |
            +---------------------+
                       |
                       |  Invoke API
                       |
                       v
            +---------------------+
            |     AWS Lambda      |
            +---------------------+
                       |
                       |  Read code and
                       |  dependencies
                       |
                       v
            +---------------------+
            |     AWS Lambda      |
            +---------------------+
                       |
                       |  Return response
                       |
                       v
            +---------------------+
            |     API Gateway     |
            +---------------------+
                       |
                       |  Response to Developer
                       v
            +---------------------+
            |      Developer      |
            +---------------------+
