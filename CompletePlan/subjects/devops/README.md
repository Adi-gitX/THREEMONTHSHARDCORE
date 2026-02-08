# 🚀 DevOps & Cloud Engineering

> **Time Allocation:** 1.5 hours/day  
> **Focus:** CI/CD, Containers, Cloud Infrastructure, Monitoring  
> **Practical Component:** Full-Stack Production Deployment

---

## 📚 Course Overview

Transform from code writer to infrastructure architect. Build, deploy, and monitor production-grade applications using industry-standard DevOps practices.

---

## 🗓️ Learning Path

### **Phase 1: Foundation (Weeks 1-3)**

#### Week 1: Version Control & CI/CD Fundamentals
- **Git Advanced**
  - Branching strategies (GitFlow, trunk-based)
  - Merge conflict resolution
  - Rebase vs merge
- **GitHub Actions**
  - Workflow YAML syntax
  - Triggers & events
  - Runners (ubuntu-latest, matrix builds)
  - Secrets & environment variables
- **CI Pipeline Components**
  - Lint → Test → Build workflow
  - Fail-fast strategies

**📝 Deliverables:**
- First GitHub Actions workflow running
- Multi-job pipeline with dependencies
- Automated testing on every push

#### Week 2: Linux & Bash Scripting
- **Essential Commands** (20+)
  - File operations, permissions
  - Text processing (grep, sed, awk)
  - Process management
- **Bash Scripting**
  - Variables, conditionals, loops
  - Functions & reusable code
  - Error handling (`set -e`)
  - Cron jobs & automation

**📝 Deliverables:**
- `deploy.sh` - Idempotent deployment script
- Backup automation
- Health check monitoring script

#### Week 3: Remote Access & Cloud Intro
- **SSH & Security**
  - SSH key generation
  - SCP file transfers
  - Remote command execution
- **AWS EC2 Basics**
  - Launch first instance
  - Security groups configuration
  - Manual Node.js deployment
- **Process Management**
  - PM2 for Node.js
  - Environment variables (`.env` files)

**📝 Deliverables:**
- Node app deployed on EC2
- Automated deployment script

---

### **Phase 2: Midsem Domination (Weeks 4-7)**

#### Week 4-5: Containerization (Docker)
**Docker Fundamentals:**
- Images vs Containers vs Volumes
- Dockerfile best practices
- Multi-stage builds (size optimization)
- Docker Compose (3+ services)
- Networking & volumes

**Practical Projects:**
```yaml
# docker-compose.yml structure
services:
  api:
    build: ./api
    environment:
      - DATABASE_URL
  postgres:
    image: postgres:14
  redis:
    image: redis:alpine
```

**📝 Deliverables:**
- Optimized Dockerfile (< 200MB)
- docker-compose for API + DB + Cache
- Container pushed to Docker Hub

#### Week 6-7: AWS Deep Dive
**Services Covered:**
- **S3:** Static website hosting
- **EC2 + Nginx:** Reverse proxy setup
- **SSL/TLS:** Let's Encrypt certificates
- **ECS:** Container orchestration
  - Task definitions
  - Services & load balancers
  - Auto-scaling
- **CloudFront:** CDN setup

**Architecture:**
```
CloudFront (CDN)
    ↓
ALB (Load Balancer)
    ↓
ECS (Container Service)
    ↓
RDS (Database)
```

**📝 Deliverables:**
- Full-stack app on AWS
- HTTPS with custom domain
- Auto-scaling configured

---

### **Phase 3: Advanced Topics (Weeks 8-11)**

#### Week 8-9: Infrastructure as Code (Terraform)
**Terraform Modules:**
```hcl
# main.tf
resource "aws_instance" "app" {
  ami           = var.ami_id
  instance_type = "t2.micro"
  
  tags = {
    Name = "production-app"
  }
}
```

**Topics:**
- `.tf` file structure
- State management (remote backends)
- Reusable modules
- VPC + Subnets + Security Groups
- Complete infrastructure in code

**📝 Deliverables:**
- Full AWS infrastructure in Terraform
- Remote state in S3
- Reusable modules

#### Week 10-11: Kubernetes & Monitoring
**Kubernetes Essentials:**
- Pods, ReplicaSets, Deployments
- Services & Ingress
- ConfigMaps & Secrets
- HPA (Horizontal Pod Autoscaler)
- Rolling updates & rollbacks

**Monitoring Stack:**
- **Prometheus:** Metrics collection
- **Grafana:** Dashboards & visualization
- **Loki:** Log aggregation
- **Alertmanager:** Alert routing

**Key Metrics:**
- Latency (P50, P95, P99)
- Error rate
- Request rate
- Resource utilization

**📝 Deliverables:**
- App deployed on Kubernetes
- Custom Grafana dashboards
- Alert rules configured
- Slack notifications

---

### **Phase 4: Production Ready (Weeks 12-13)**

#### Week 12: Load Testing & Performance
**Tools:**
- **Locust:** Python-based load testing
  - 100+ RPS testing
  - Performance bottleneck identification

**Optimization:**
- Redis caching layer
- Database query optimization
- CDN for static assets

**📝 Deliverables:**
- Load test results (100 RPS sustained)
- Performance analysis report
- Optimization recommendations

#### Week 13: Final Polish
**Documentation:**
- Architecture diagrams (professional quality)
- Deployment runbook
- Failure recovery procedures
- API documentation (Swagger/OpenAPI)

**Security:**
- Trivy container scanning
- Dependabot alerts
- Secret management (HashiCorp Vault)
- Security group hardening

**📝 Final Deliverables:**
- Complete CI/CD pipeline (Lint → Test → Build → Deploy → Monitor)
- Production-grade application
- 3-minute demo video
- Blog post on Medium/Hashnode
- Professional architecture diagram

---

## 🛠️ Technology Stack

### Core Technologies
- **Version Control:** Git, GitHub
- **CI/CD:** GitHub Actions
- **Containers:** Docker, Docker Compose, Kubernetes
- **Cloud:** AWS (EC2, ECS, S3, CloudFront, RDS, VPC)
- **IaC:** Terraform, CloudFormation
- **Monitoring:** Prometheus, Grafana, Loki
- **Load Testing:** Locust
- **Security:** Trivy, Dependabot, Vault

### Languages
- Bash scripting
- YAML (workflows, compose, k8s)
- HCL (Terraform)
- Python (automation, load testing)

---

## 📊 Project Timeline

### Major Project Builds (Saturdays)
- **Day 8:** Dataset + Architecture documentation
- **Day 15:** PyTorch training script
- **Day 22:** MLflow experiments
- **Day 29:** FastAPI endpoint
- **Day 36:** Validation + logging
- **Day 43:** Dockerfile + Compose
- **Day 50:** CI/CD pipeline
- **Day 57:** Terraform infrastructure
- **Day 64:** Monitoring (Prometheus + Grafana)
- **Day 71:** Load testing setup
- **Day 78:** Architecture diagram

---

## 🎯 Success Metrics

- [ ] GitHub Actions pipeline running (100% test coverage)
- [ ] Docker container < 200MB
- [ ] Application deployed on AWS (HTTPS)
- [ ] Kubernetes deployment working
- [ ] Infrastructure 100% in Terraform
- [ ] Grafana dashboards operational
- [ ] Load test: 100 RPS sustained
- [ ] Blog post published
- [ ] Demo video recorded
- [ ] Zero production incidents

---

## 📚 Resources

### Essential Learning
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [Terraform Documentation](https://www.terraform.io/docs)
- [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)

### Practice Platforms
- [KodeKloud](https://kodekloud.com/) - DevOps labs
- [Play with Docker](https://labs.play-with-docker.com/)
- [Katacoda](https://www.katacoda.com/) - Interactive scenarios

### Certification Paths (Optional)
- AWS Certified Solutions Architect
- Certified Kubernetes Administrator (CKA)
- HashiCorp Terraform Associate

---

## 💡 Best Practices

### CI/CD Pipeline
```yaml
name: Production Deployment

on:
  push:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Lint code
        run: npm run lint
  
  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: npm test
  
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Build Docker image
        run: docker build -t app:${{ github.sha }} .
  
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to production
        run: ./deploy.sh
```

### Docker Best Practices
- Use multi-stage builds
- Minimize layers
- Don't run as root
- Use `.dockerignore`
- Tag images with version/SHA

### Terraform Best Practices
- Use remote state
- Module everything
- Pin provider versions
- Use variables & outputs
- Never commit secrets

---

## 🔗 Related Resources

- [Back to Complete Plan](../../README.md)
- [Operating Systems](../operating-systems/)
- [Projects](../../projects/)

---

**Remember:** DevOps is about culture, automation, and reliability. Build systems that scale!

*Last Updated: Day 0*
