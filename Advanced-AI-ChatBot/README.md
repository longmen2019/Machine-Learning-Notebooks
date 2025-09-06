```markdown
# 🤖 Chatbot Assistant with Intent Classification

A modular, trainable chatbot built using PyTorch and NLTK for intent classification. This assistant parses structured intents from a JSON file, tokenizes and vectorizes user input, and uses a feedforward neural network to predict the most relevant intent. It supports both static responses and dynamic function mappings for extensible behavior.

---

## 🚀 Features

- **Intent Parsing**: Loads and processes intents from a JSON file.
- **Text Normalization**: Tokenizes and lemmatizes input using NLTK.
- **Bag-of-Words Vectorization**: Converts input into binary vectors based on vocabulary presence.
- **Model Training**: Trains a PyTorch model using CrossEntropyLoss and Adam optimizer.
- **Model Persistence**: Saves and loads model weights and dimensions.
- **Dynamic Function Mapping**: Supports custom functions for specific intents (e.g., stock lookup).
- **Interactive CLI**: Allows real-time user interaction via terminal.

---

## 📁 Project Structure

```
chatbot/
│
├── intents.json              # JSON file defining intents, patterns, and responses
├── chatbot_model.pth         # Saved PyTorch model weights
├── dimensions.json           # Metadata for input/output dimensions
├── chatbot.py                # Main assistant class and training logic
├── model.py                  # Neural network definition (ChatbotModel)
└── run.py                    # CLI interface for training and interaction
```

---

## 🧠 How It Works

1. **Intents Parsing**  
   Loads structured data from `intents.json` and extracts patterns, tags, and responses.

2. **Preprocessing**  
   Tokenizes and lemmatizes each pattern to build a consistent vocabulary.

3. **Vectorization**  
   Converts each pattern into a bag-of-words vector for training.

4. **Model Training**  
   Trains a simple feedforward neural network to classify intents.

5. **Inference**  
   Predicts the intent of user input and returns a mapped response or executes a custom function.

---

## 🛠️ Setup

```bash
pip install torch nltk numpy
python -m nltk.downloader punkt wordnet
```

---

## 🧪 Example Usage

```bash
python run.py
```

```text
Enter your message: show me some stocks
['META', 'NVDA', 'GS']
```

---

## 🧩 Extending Functionality

You can map any intent to a custom Python function:

```python
def get_stocks():
    return random.sample(['AAPL', 'META', 'NVDA', 'GS', 'MSFT'], 3)

assistant = ChatbotAssistant('intents.json', function_mappings={'stocks': get_stocks})
```

---

## 📌 Notes

- Make sure to correct `'APPL'` to `'AAPL'` in your stock list.
- The model uses raw logits; no softmax is applied since `CrossEntropyLoss` expects it.
- Dropout is used during training to improve generalization.

---

## 📄 License

MIT License. Feel free to use, modify, and distribute.

---

## 👨‍💻 Author

Built by Long — Cloud Architect & DevOps Engineer specializing in modular automation, CI/CD, and scalable infrastructure.

