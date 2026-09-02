# Ecommerce ETL Pipeline 

This is a project for CI/CD automation of ETL pipeline using GitHub Actions CI/CD and to automate the building of docker images and pushing docker image to dockerhub and use it for kubernetes to create and orchestrate docker containers in pods

## Tech Stacks Used:-

1. Python
2. Streamlit
3. Github Actions CI/CD - through .github/workflows/ci-cd-automation.yaml 
4. Docker
5. Kubernetes

## Project Architecture

![Architecture of Project](images/architecture.png)

## Project Deployment Images (AWS - Cluster)

![eks cluster](images/eks-cluster.png)

## Project Deployment Images (AWS - Load Balancer img)
![load balancer image](images/load-balancer.png)

![eks cluster](images/eks-cluster.png)

## Project Deployment Images (App Image)

![Apps Image](images/app-image.png)

deployment link -> http://k8s-default-ecommerc-11d52b9d07-bce751d49d2d1556.elb.ap-south-2.amazonaws.com

## Project Deployment Images (AWS - CloudWatch -> logs & dashboard - imgs)

1. cluster logs - from cloudwatch
![cluster logs](images/cluster-logs.png)



2. cluster log streams - from cloudwatch
![cluster log streams](images/cluster-log-streams.png)



3. cluster dashboard
![cluster dashboard](images/cluster-dashboard.png)



4. cluster observability dashboard
![cluster observability dashboard](images/cluster-observability-dashboard.png)



5. node health status
![node health](images/node-health.png)



6. node dashboard
![node dashboard](images/node-dashboard1.png)



7. pod dashboard
![pod dashboard](images/pod-dashboard1.png)



8. service dashboard
![service dashboard](images/service-dashboard1.png)