# AWS Projects
Repository for compiling my studies in AWS


## Caption
The directories are organized following this logic:
* The directory starts with a number that represents the order that I made the project. It's not going to represent the complexity, but the order of studies;
* The second part represents the main area of the project. It can be: "ML (Machine Learning)", "DS (Data Science and Data Analysis)", "AI (Artificial Intelligence - Agentic AI, Computer Vision, LLMs, etc.)", "OT (Everything else that doesn't fit on the other categories)";
* The last parts: They're the AWS services that I'm using on this project

---
# Concepts

## What is AWS?
Amazon Web Services (AWS) is a cloud computing services platform offered by Amazon, providing a wide range of on-demand IT infrastructure services to businesses, developers, and governments on a pay-as-you-go model. Launched in 2006, AWS pioneered the concept of offering cloud computing services, becoming one of the leading cloud providers in the global market.<br/>
AWS services span various categories, including computing, storage, databases, networking, machine learning, data analytics, application development, security, the Internet of Things (IoT), and more. These services allow users to create and manage scalable IT infrastructures, develop and deploy applications, perform data analytics, and execute a wide variety of other computing functions without the need to invest in physical hardware. <br/>
Some of AWS's best-known offerings include Amazon Elastic Compute Cloud (EC2), which allows users to rent virtual servers to run applications; Amazon Simple Storage Service (S3), for scalable data storage; and Amazon RDS for database management. and Amazon Sagemaker for building, training, and deploying machine learning models. <br/>
AWS operates in multiple geographic regions around the world, each comprised of several availability zones, ensuring high availability, reliability, and data security. With its vast range of services and global network of data centers, AWS provides businesses of all sizes with the infrastructure they need to innovate rapidly, scale their systems, and operate more efficiently and securely in the cloud. Access the official website at the link below:<br/>
* https://aws.amazon.com/


## What is WSGI (Web Server Gateway Interface)?
WSGI, an acronym for Web Server Gateway Interface, is a specification for a simple interface between web servers and web applications or frameworks for the Python programming language. Defined by PEP 3333, WSGI was created as a standard to facilitate communication between web software components, allowing for greater interoperability and flexibility in the development of Python web applications.<br/>

The central idea of WSGI is to define a common interface that allows web applications to run on top of various web servers without the need for changes to the application code. This means that developers can choose between different web servers (such as Apache, Nginx with WSGI modules, or dedicated servers like Gunicorn or uWSGI) and web frameworks (such as Django, Flask, Pyramid, etc.) without worrying about incompatibilities between the application and the server.<br/>

A WSGI application is simply a "callable" Python object (such as a function or a method) that accepts two parameters: a dictionary containing environment variables (which includes HTTP request data) and a callback function to start the HTTP response. The application then returns the response data in an iterable. This allows the web application to be written in a modular and reusable way, following the principles of the WSGI interface.<br/>

The adoption of WSGI as a standard in Python web development has brought great flexibility to the community, allowing for a rich ecology of frameworks and web servers, as well as facilitating the composition of applications with components from different sources. This has promoted a more dynamic and innovative web development environment within the Python ecosystem.<br/>