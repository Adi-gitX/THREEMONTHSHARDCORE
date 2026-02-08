# 🧠 Deep Learning & Applied Machine Learning

> **Time Allocation:** 1.25 hours/day  
> **Focus:** Neural Networks, CNNs, RNNs, Transformers, Statistical ML  
> **Practical Component:** Production ML Model Deployment

---

## 📚 Course Overview

Build deep learning systems from scratch. Progress from basic neural networks to state-of-the-art Transformer architectures, with a strong emphasis on mathematical foundations and practical implementation.

---

## 🗓️ Learning Path

### **Phase 1: Foundation (Weeks 1-3)**

#### Week 1: Mathematical Foundations
**Linear Algebra:**
- PCA (Principal Component Analysis)
  - Eigenvalues & eigenvectors
  - Dimensionality reduction
  - NumPy implementation
- SVD (Singular Value Decomposition)
- Matrix operations & transformations

**Probability & Information Theory:**
- Entropy & information gain
- Cross-entropy loss
- KL Divergence
- Bayesian inference

**📝 Deliverables:**
- PCA implementation from scratch
- Information theory notebook

#### Week 2: Neural Network Basics
**Building Blocks:**
- Perceptron from scratch
- Forward propagation
- Activation functions
  - Sigmoid, tanh, ReLU, Leaky ReLU
  - Comparison & use cases
- Loss functions
  - MSE, Cross-entropy
  - When to use which

**Backpropagation:**
- Chain rule & computational graphs
- Manual gradient computation
- Vanishing/exploding gradients

**Code:**
```python
class NeuralNetwork:
    def __init__(self, layers):
        self.weights = []
        self.biases = []
        self._initialize_parameters(layers)
    
    def forward(self, X):
        # Implement forward pass
        pass
    
    def backward(self, X, y):
        # Implement backpropagation
        pass
```

**📝 Deliverables:**
- XOR problem solved with multi-layer network
- Backprop implementation from scratch (NumPy)

#### Week 3: Optimization & Regularization
**Optimizers:**
- SGD (Stochastic Gradient Descent)
- Momentum
- Adam optimizer
  - Implementation from scratch
  - Hyperparameter tuning

**Regularization:**
- L1/L2 regularization
- Dropout implementation
- Batch Normalization
- Layer Normalization
- Data augmentation pipeline

**📝 Deliverables:**
- Optimizer comparison benchmarks
- Regularization techniques notebook

---

### **Phase 2: Convolutional Neural Networks (Weeks 4-7)**

#### Week 4-5: CNN Architecture
**Fundamentals:**
- Conv2D operation from scratch
- Pooling layers (Max, Average)
- Feature maps visualization
- Receptive fields

**Architectures:**
- LeNet
- AlexNet concepts
- VGG patterns
- ResNet & skip connections

**Practical:**
```python
# MNIST CNN (98%+ accuracy target)
model = Sequential([
    Conv2D(32, 3, activation='relu'),
    MaxPooling2D(2),
    Conv2D(64, 3, activation='relu'),
    MaxPooling2D(2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])
```

**📝 Deliverables:**
- Conv2D implementation from scratch
- MNIST classifier (98%+ accuracy)
- Feature map visualization

#### Week 6-7: Advanced CNN Topics
**Transfer Learning:**
- Pre-trained models (VGG, ResNet)
- Fine-tuning strategies
- Feature extraction

**Object Detection:**
- Bounding boxes
- IoU (Intersection over Union)
- Basic detection concepts

**📝 Deliverables:**
- Transfer learning project
- Custom dataset classifier

---

### **Phase 3: Recurrent Networks & Sequences (Weeks 8-11)**

#### Week 8-9: RNN, LSTM, GRU
**Sequential Models:**
- Vanilla RNN implementation
- LSTM from scratch
  - Forget gate, input gate, output gate
  - Cell state updates
- GRU architecture
- Comparison: RNN vs LSTM vs GRU

**Applications:**
- Time series prediction
- Sequence classification
- Text generation

**📝 Deliverables:**
- LSTM implementation from scratch
- Time series forecasting notebook

#### Week 10-11: Attention & Transformers
**Attention Mechanism:**
- Self-attention from scratch
- Multi-head attention
- Positional encoding
- Scaled dot-product attention

**Transformer Architecture:**
```
Encoder:
  - Multi-Head Self-Attention
  - Feed-Forward Network
  - Layer Normalization
  - Residual Connections

Decoder:
  - Masked Self-Attention
  - Cross-Attention
  - Feed-Forward Network
```

**Implementations:**
- Attention mechanism from scratch
- Transformer encoder block
- Transformer decoder block

**Pre-trained Models:**
- BERT architecture study
- GPT architecture study
- Fine-tuning with HuggingFace

**📝 Deliverables:**
- Full Transformer implementation
- HuggingFace fine-tuning project
- Attention visualization

---

### **Phase 4: Applied ML & Production (Weeks 12-13)**

#### Statistical Machine Learning
**Clustering:**
- K-Means from scratch
- DBSCAN implementation
- Hierarchical clustering

**Support Vector Machines:**
- Linear SVM margin derivation
- RBF kernel
- Hard vs soft margin (C parameter)
- Grid search for hyperparameters

**Time Series:**
- Stationarity & ADF test
- ACF/PACF plot analysis
- ARIMA(p,d,q) fitting
- Model selection (AIC/BIC)

**Ensemble Methods:**
- Bagging & boosting
- Random Forest implementation
- XGBoost deep dive
- Stacking ensemble

**Bayesian Methods:**
- Bayesian networks structure
- Markov chains & HMM
- Forward algorithm
- Viterbi decoding
- Baum-Welch training

**📝 Deliverables:**
- Complete statistical ML library
- Time series forecasting project

#### Production ML
**Experiment Tracking:**
- MLflow setup
- Experiment logging
- Hyperparameter sweeps
- Model versioning

**Model Deployment:**
- FastAPI endpoint creation
- Input validation (Pydantic)
- Response time optimization (< 200ms)
- Docker containerization

**Monitoring:**
- Model drift detection (Evidently)
- Performance metrics tracking
- Alert configuration

**📝 Final Deliverables:**
- ML model deployed to production
- Monitoring dashboards
- Complete MLOps pipeline

---

## 🛠️ Technology Stack

### Frameworks & Libraries
- **NumPy:** Low-level implementations
- **PyTorch:** Deep learning framework
- **TensorFlow/Keras:** Alternative framework
- **HuggingFace:** Pre-trained transformers
- **MLflow:** Experiment tracking
- **FastAPI:** Model serving
- **Evidently:** Model monitoring

### Tools
- **Jupyter:** Interactive development
- **TensorBoard:** Visualization
- **Weights & Biases:** Experiment tracking
- **Docker:** Containerization

---

## 📊 Project Timeline

### Major Builds
- **Day 8:** Dataset acquisition & EDA
- **Day 15:** PyTorch training script
- **Day 22:** MLflow experiments
- **Day 29:** FastAPI endpoint
- **Day 36:** Validation & logging
- **Day 43:** Docker deployment
- **Day 50:** CI/CD integration
- **Day 57:** AWS deployment
- **Day 64:** Monitoring setup

---

## 🎯 Success Metrics

### Technical Skills
- [ ] Neural network from scratch (NumPy)
- [ ] Backpropagation implemented manually
- [ ] MNIST CNN (98%+ accuracy)
- [ ] LSTM from scratch
- [ ] Transformer implemented
- [ ] HuggingFace fine-tuning complete
- [ ] Model deployed to production
- [ ] FastAPI response time < 200ms

### Projects
- [ ] 3+ datasets processed
- [ ] Image classification (98%+ accuracy)
- [ ] Time series forecasting
- [ ] Text generation model
- [ ] Production deployment with monitoring

---

## 📚 Resources

### Essential Books
- **Deep Learning** by Goodfellow, Bengio, Courville
- **Pattern Recognition & ML** by Bishop
- **Hands-On Machine Learning** by Géron

### Online Courses
- [Fast.ai](https://www.fast.ai/) - Practical deep learning
- [CS231n](http://cs231n.stanford.edu/) - CNNs for Visual Recognition
- [CS224n](http://web.stanford.edu/class/cs224n/) - NLP with Deep Learning

### Papers to Read
- "Attention Is All You Need" (Transformer)
- "Deep Residual Learning" (ResNet)
- "BERT: Pre-training of Deep Bidirectional Transformers"
- "Language Models are Few-Shot Learners" (GPT-3)

### Coding Resources
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [HuggingFace Course](https://huggingface.co/course)
- [Papers with Code](https://paperswithcode.com/)

---

## 💡 Study Techniques

### 1. **Implement from Scratch**
Always code the fundamentals without frameworks first:
```python
# Bad: Just using PyTorch
model = nn.Linear(10, 1)

# Good: Understanding the math
def linear_forward(X, W, b):
    return np.dot(X, W) + b

def linear_backward(dout, X, W):
    dW = np.dot(X.T, dout)
    db = np.sum(dout, axis=0)
    dX = np.dot(dout, W.T)
    return dX, dW, db
```

### 2. **Visualize Everything**
- Plot loss curves
- Visualize feature maps
- Show attention weights
- Display gradients

### 3. **Ablation Studies**
Test each component:
- Remove batch norm → observe effect
- Change optimizer → compare convergence
- Vary learning rate → plot results

### 4. **Code Review Pattern**
For each topic:
1. Understand math (derive on paper)
2. Implement from scratch (NumPy)
3. Implement with framework (PyTorch)
4. Apply to real dataset
5. Debug & optimize

---

## 📝 Notes Template

```markdown
## [Topic: e.g., LSTM]

### Mathematical Foundation
- Equations (LaTeX)
- Derivations

### Key Insights
- Why does it work?
- When to use?
- Limitations?

### Implementation
```python
# Code here
```

### Experiments
| Config | Loss | Accuracy | Notes |
|--------|------|----------|-------|
| ...    | ...  | ...      | ...   |

### Questions
- Open questions
- Things to explore
```

---

## 🔗 Related Resources

- [Back to Complete Plan](../../README.md)
- [DSA](../dsa/)
- [Projects](../../projects/)

---

**Remember:** Deep learning is 10% inspiration, 90% debugging. Embrace the struggle!

*Last Updated: Day 0*
