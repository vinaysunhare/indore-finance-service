# Indore Finance Service

![indore-finance-home1](https://github.com/user-attachments/assets/3a9aefcf-bd3b-4469-86d3-4ec89e86a04a)
![indorefinancehome2](https://github.com/user-attachments/assets/e3966091-5a8e-42e6-b23d-53d9ea6200f7)
![indorefinancehome3](https://github.com/user-attachments/assets/52a4d646-1389-4947-b555-9f4e5fc4a7c9)
![indorefinanceloan1](https://github.com/user-attachments/assets/9f293358-a792-460e-911f-bacf587941d6)
![indorefinanceinvestment1](https://github.com/user-attachments/assets/18ed51ef-3dd1-43c3-b7d9-787f977c5096)
![indorefinanceinvestmenttracker2](https://github.com/user-attachments/assets/dd12f506-12e6-454c-804c-45ccac128812)
![indorefinancecontact1](https://github.com/user-attachments/assets/e3cf9968-2e94-4e22-aa1a-dea24731b541)
![indorefinancecontact2](https://github.com/user-attachments/assets/78d50385-3008-438a-b7fa-0fbf965e3693)
![Screenshot from 2025-04-27 18-35-36](https://github.com/user-attachments/assets/4b0b7cf9-c9b8-4dfb-a4da-3292d9220570)
![Screenshot from 2025-04-27 18-14-56](https://github.com/user-attachments/assets/83487a64-c575-45e6-933c-2e647e09458e)
![Screenshot from 2025-04-27 18-36-01](https://github.com/user-attachments/assets/2fe4bd5c-6529-4ca0-b7d8-3846c56e04d6)
![Screenshot from 2025-04-27 18-36-28](https://github.com/user-attachments/assets/6b74c86e-d0d6-4901-bf50-69549d11c979)
![Screenshot from 2025-04-27 18-36-47](https://github.com/user-attachments/assets/3c63021a-d5b2-4a13-9bf5-b5fce2f276eb)



# Indore Finance Service Deployment Guide

**GitHub Repository**: [https://github.com/vinaysunhare/indore-finance-service](https://github.com/vinaysunhare/indore-finance-service)

This document outlines the process of cloning, setting up, deploying, and monitoring the **Indore Finance Service** web application using modern DevOps tools, including Docker, Kubernetes, Jenkins, Prometheus, and Grafana.

---

## 1. Cloning and Local Setup

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vinaysunhare/indore-finance-service.git
   cd indore-finance-service
   ```

2. **Run the Application**:
   ```bash
   python run.py
   ```

3. **Install Dependencies** (if errors occur):
   ```bash
   sudo apt install python-is-python3
   pip3 install flask
   ```

4. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   pip install flask
   ```

5. **Run Again**:
   ```bash
   python run.py
   ```

---

## 2. Dockerizing the Application

### Steps
1. **Create `Dockerfile`**:
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   EXPOSE 5000
   ENV FLASK_APP=app.py
   ENV FLASK_RUN_HOST=0.0.0.0
   CMD ["flask", "run", "--host=0.0.0.0"]
   ```

2. **Install Docker**:
   ```bash
   sudo apt update
   sudo apt install docker.io -y
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

3. **Add User to Docker Group**:
   ```bash
   sudo usermod -aG docker $USER
   newgrp docker
   ```

4. **Build and Run Docker Image**:
   ```bash
   docker build -t indore-finance-service .
   docker run --rm -p 5000:5000 indore-finance-service
   ```

5. **Test Application**:
   Visit `http://172.17.0.4:5000/` in a browser.

---

## 3. Deploying to Kubernetes with Minikube

### Steps
1. **Install Minikube**:
   ```bash
   sudo apt update
   sudo apt install curl -y
   curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
   sudo install minikube-linux-amd64 /usr/local/bin/minikube
   ```

2. **Start Minikube**:
   ```bash
   minikube start
   ```

3. **Create `deployment.yaml`**:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: indore-finance-deployment
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: indore-finance-service
     template:
       metadata:
         labels:
           app: indore-finance-service
       spec:
         containers:
         - name: indore-finance-service
           image: vinaysunhare/indore-finance-service:latest
           ports:
           - containerPort: 5000
   ```

4. **Create `service.yaml`**:
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: indore-finance-service
   spec:
     selector:
       app: indore-finance-service
     ports:
     - protocol: TCP
       port: 80
       targetPort: 5000
     type: LoadBalancer
   ```

5. **Apply Configurations**:
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

6. **Verify Deployment**:
   ```bash
   kubectl get deployments
   kubectl get services
   ```

7. **Access Application**:
   ```bash
   minikube service indore-finance-service
   ```

---

## 4. Setting Up Jenkins for CI/CD

### Steps
1. **Install Jenkins**:
   ```bash
   sudo apt update -y && sudo apt upgrade -y
   sudo apt install openjdk-21-jdk -y
   sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
   echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
   sudo apt update -y
   sudo apt install jenkins -y
   sudo systemctl start jenkins
   sudo systemctl enable jenkins
   ```

2. **Access Jenkins**:
   - Go to `http://localhost:8080`.
   - Get the initial password:
     ```bash
     sudo cat /var/lib/jenkins/secrets/initialAdminPassword
     ```

3. **Install Plugins**:
   - Navigate to **Dashboard > Manage Jenkins > Plugins**.
   - Install: Git Plugin, Pipeline Plugin, Docker Plugin, Blue Ocean, Maven Integration.

4. **Install Maven**:
   ```bash
   sudo apt update
   sudo apt install maven -y
   mvn -version
   ```

5. **Create Pipeline**:
   - Go to **New Item > Pipeline**.
   - Configure to pull from `https://github.com/vinaysunhare/indore-finance-service`.
   - Add a `pom.xml` for Maven builds and push to GitHub.

6. **Configure Maven in Jenkins**:
   - Go to **Dashboard > Manage Jenkins > Global Tool Configuration > Maven > Add Maven Installation**.

---

## 5. Updating Code and Testing CI/CD

### Steps
1. **Update Code**:
   - Change the title in the Flask app from `"Expert Financial Services in Indore"` to `"Expert Financial Services in Indore, Madhya Pradesh"`.
   - Commit and push:
     ```bash
     git add .
     git commit -m "Updated title"
     git push origin master
     ```

2. **Rebuild Docker Image**:
   ```bash
   docker build -t vinaysunhare/indore-finance-service:latest .
   docker push vinaysunhare/indore-finance-service:latest
   ```

3. **Update `deployment.yaml`**:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: indore-finance-service
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: indore-finance-service
     template:
       metadata:
         labels:
           app: indore-finance-service
       spec:
         containers:
         - name: indore-finance-service
           image: vinaysunhare/indore-finance-service:latest
           imagePullPolicy: Never
           ports:
           - containerPort: 5000
   ```

4. **Apply and Restart**:
   ```bash
   kubectl apply -f deployment.yaml
   kubectl rollout restart deployment/indore-finance-deployment
   ```

5. **Verify**:
   ```bash
   minikube service indore-finance-service --url
   ```

6. **Run Jenkins Pipeline**:
   - Trigger a build in Jenkins and confirm the updated title appears on the live server.

---

## 6. Monitoring with Prometheus and Grafana

### Steps
1. **Install Helm**:
   ```bash
   curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
   ```

2. **Add Prometheus Repository**:
   ```bash
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo update
   ```

3. **Install Prometheus and Grafana**:
   ```bash
   helm install monitoring prometheus-community/kube-prometheus-stack
   ```

4. **Check Pods**:
   ```bash
   kubectl get pods -l "release=monitoring"
   ```

5. **Access Grafana**:
   - Get password:
     ```bash
     kubectl get secret monitoring-grafana -o jsonpath="{.data.admin-password}" | base64 -d
     ```
   - Port-forward:
     ```bash
     kubectl port-forward svc/monitoring-grafana 3000:80
     ```
   - Log in at `http://localhost:3000` (username: `admin`).

6. **Add Prometheus Metrics to Flask**:
   - Install exporter:
     ```bash
     pip install prometheus-flask-exporter
     ```
   - Update `run.py`:
     ```python
     from app import create_app
     from prometheus_flask_exporter import PrometheusMetrics

     app = create_app()
     metrics = PrometheusMetrics(app)

     @app.route('/')
     def hello():
         return "Indore Finance Service is up and running!"

     if __name__ == "__main__":
         app.run(host='0.0.0.0', port=5000, debug=True)
     ```

7. **Update `requirements.txt`**:
   ```text
   blinker==1.9.0
   click==8.1.7
   Flask==3.1.0
   itsdangerous==2.2.0
   Jinja2==3.1.4
   MarkupSafe==3.0.2
   Werkzeug==3.1.3
   prometheus-flask-exporter==0.23.2
   ```

8. **Rebuild and Push Image**:
   ```bash
   docker build -t vinaysunhare/indore-finance-service:latest .
   docker push vinaysunhare/indore-finance-service:latest
   ```

9. **Create Prometheus ConfigMap** (`prometheus-config.yaml`):
   ```yaml
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: prometheus-config
   data:
     prometheus.yml: |
       global:
         scrape_interval: 15s
       scrape_configs:
       - job_name: 'indore-finance-service'
         static_configs:
         - targets: ['indore-finance-service.default.svc.cluster.local:5000']
   ```

10. **Deploy Prometheus** (`prometheus-deployment.yaml`):
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: prometheus-deployment
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: prometheus
      template:
        metadata:
          labels:
            app: prometheus
        spec:
          containers:
          - name: prometheus
            image: prom/prometheus
            args:
              - "--config.file=/etc/prometheus/prometheus.yml"
            ports:
              - containerPort: 9090
            volumeMounts:
              - name: prometheus-config-volume
                mountPath: /etc/prometheus
          volumes:
            - name: prometheus-config-volume
              configMap:
                name: prometheus-config
    ```

11. **Expose Prometheus** (`prometheus-service.yaml`):
    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: prometheus-service
    spec:
      selector:
        app: prometheus
      ports:
      - protocol: TCP
        port: 9090
        targetPort: 9090
      type: NodePort
    ```

12. **Apply Configurations**:
    ```bash
    kubectl apply -f prometheus-config.yaml
    kubectl apply -f prometheus-deployment.yaml
    kubectl apply -f prometheus-service.yaml
    ```

13. **Access Prometheus**:
    ```bash
    minikube service prometheus-service --url
    ```

14. **Fix Metrics 404 Error**:
    - Update `__init__.py`:
      ```python
      from flask import Flask
      from prometheus_flask_exporter import PrometheusMetrics

      def create_app():
          app = Flask(__name__)
          app.config['SECRET_KEY'] = 'your_secret_key'
          metrics = PrometheusMetrics(app)
          with app.app_context():
              from .routes import main_bp
              app.register_blueprint(main_bp)
          return app
      ```
    - Update `routes.py`:
      ```python
      from flask import Blueprint, render_template, request

      main_bp = Blueprint("main", __name__)

      @main_bp.route("/")
      def home():
          return render_template("home.html")

      @main_bp.route("/loan-calculator", methods=["GET", "POST"])
      def loan_calculator():
          if request.method == "POST":
              amount = float(request.form["amount"])
              interest = float(request.form["interest"])
              years = int(request.form["years"])
              monthly_rate = interest / 100 / 12
              months = years * 12
              monthly_payment = (amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
              return render_template("loan_calculator.html", payment=round(monthly_payment, 2))
          return render_template("loan_calculator.html", payment=None)

      @main_bp.route("/investment-tracker")
      def investment_tracker():
          return render_template("investment_tracker.html")

      @main_bp.route("/contact")
      def contact():
          return render_template("contact.html")

      @main_bp.route("/health")
      def health():
          return "OK", 200
      ```

15. **Rebuild and Redeploy**:
    ```bash
    docker build -t vinaysunhare/indore-finance-service:latest .
    docker push vinaysunhare/indore-finance-service:latest
    kubectl apply -f deployment.yaml
    kubectl rollout restart deployment/indore-finance-deployment
    ```

16. **Set Grafana Password**:
    - Encode password (`vinaysunhare`):
      ```bash
      echo -n 'vinaysunhare' | base64
      ```
    - Patch secret:
      ```bash
      kubectl patch secret grafana -n monitoring -p '{"data": {"admin-password": "dmluYXlzdW5oYXJl"}}'
      ```

17. **Access Grafana**:
    ```bash
    kubectl port-forward svc/grafana -n monitoring 3000:80
    ```
    Log in at `http://localhost:3000`.

18. **Add Prometheus Data Source**:
    - Port-forward Prometheus:
      ```bash
      kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090 -n default
      ```
    - Add URL `http://monitoring-kube-prometheus-prometheus.default.svc.cluster.local:9090` in Grafana.

19. **Explore Dashboards**:
    - View prebuilt dashboards in **Dashboards > Manage** (e.g., Kubernetes / Compute Resources).

---

## 7. Benefits of This Setup

- **Automation**: CI/CD with Jenkins automates builds and deployments.
- **Portability**: Docker ensures consistent app behavior across environments.
- **Scalability**: Kubernetes enables auto-scaling and high availability.
- **Reliability**: Stable deployments with zero-downtime updates.
- **Monitoring**: Prometheus and Grafana provide real-time insights and alerts.
- **Career Growth**: Industry-standard tools enhance DevOps skills.

---

## 8. Future Enhancements

- **CI/CD**: Add multi-stage pipelines, automated tests, and Blue-Green deployments.
- **Kubernetes**: Implement autoscaling, Helm Charts, and Service Mesh.
- **Security**: Use RBAC, secure Docker images, and vulnerability scanning.
- **Monitoring**: Set up alerts and custom dashboards.
- **High Availability**: Deploy multi-cluster setups and load balancers.
- **GitOps**: Manage deployments with ArgoCD or FluxCD.

---

## License

This project is licensed under the **MIT License**. For more details, refer to the `LICENSE` file included in the repository.

---
## Thank You God
---
## Contact

For further information or queries, reach out to:

- **Author**: Vinay Sunhare  
- **Email**: [vinaysunhare25@gmail.com](mailto:vinaysunhare25@gmail.com)  
- **LinkedIn**: [Vinay Sunhare on LinkedIn](https://www.linkedin.com/in/vinay-sunhare)  
- **GitHub Repository**: [Indore Finance Service](https://github.com/vinaysunhare/indore-finance-service)
