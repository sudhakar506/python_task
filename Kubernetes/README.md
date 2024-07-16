## Deploy Kubernetes - Commands
 - kubectl apply -f project_deploy.yaml
 
### Command Results
  - deployment.apps/project_deploy-demo created
  - service/project_deploy-entrypoint created

### Check Kubernetes Deployment Status
  -kubectl get deployments

### Kubernetes Status Results
  - NAME                 READY   UP-TO-DATE    AVAILABLE   AGE
  - project_deploy-demo   1/1     1            1           40s

### Kubernetes Status Results
  - kubectl get services
 
### Kubernetes yaml Results
  - NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
  - project_deploy-entrypoint   NodePort    10.106.145.116   <none>        3000:30001/TCP   53s
  - kubernetes                  ClusterIP   10.96.0.1        <none>        443/TCP          138d


### To See The Kubernetes Server
  - localhost:30001

### Tear Down Kubernetes Session
  - kubectl delete -f bb.yaml