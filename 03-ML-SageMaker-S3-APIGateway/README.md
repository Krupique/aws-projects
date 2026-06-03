# MLOps: From Business Problem to Deployment with SageMaker, Lambda Function, and API Gateway

### Bucket S3
The first thing we need to to is create a bucket on AWS S3.
   * Use your account ID in your bucket name because the name of the bucket is global;
   * My bucket: s3://03-ml-351371806175

Upload the dataset.csv to your bucket

### SageMaker AI
1. Open the service Amazon SageMaker AI and then click in domains;
2. Select or create a new domain and click Open Studio;

**SageMaker Studio**<br/>
* On this page, open the Jubyterlab and create a new space or select one.
* In your space, select the machine config and then click in Run Space.