# 🧪 Cross-Browser Automation Testing using Selenium & BrowserStack

## 📌 Project Overview

This project demonstrates an **end-to-end cross-browser automation testing framework** built using **Selenium WebDriver (Python)** and **BrowserStack Cloud**.

The goal is to automate critical user flows (login and form validation) and execute the **same test logic across multiple real browsers and operating systems** using BrowserStack’s cloud infrastructure.

This project simulates a **real-world QA / SDET workflow**, starting from local validation and scaling to cloud-based cross-browser testing.

---

## 🎯 Objectives

- Automate UI test cases using Selenium WebDriver
- Validate tests locally before cloud execution
- Execute tests on real browsers using BrowserStack Automate
- Demonstrate cross-browser compatibility without changing test logic
- Follow industry best practices (environment variables, clean structure, documentation)

---

## 🏗️ Project Structure

```
Cross-Browser Automation Testing using Selenium & BrowserStack/
│
├── config/
│   ├── __init__.py
│   └── browserstack_config.py
│
├── tests/
│   ├── __init__.py
│   └── test_login2.py
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

- Python 3
- Selenium WebDriver
- BrowserStack Automate
- webdriver-manager
- Git & GitHub

---

## 🌐 Test Application Used

- https://the-internet.herokuapp.com/login  
- Username: `tomsmith`  
- Password: `SuperSecretPassword!`

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### `requirements.txt`
```
selenium
webdriver-manager
```

---

## 3️⃣ BrowserStack Credentials Setup (IMPORTANT)

BrowserStack authentication is handled securely using **environment variables**.

### 🔹 Windows (CMD / PowerShell)
```bash
setx BROWSERSTACK_USERNAME "your_browserstack_username"
setx BROWSERSTACK_ACCESS_KEY "your_browserstack_access_key"
```

➡️ Close and reopen the terminal after running the above commands.

### 🔹 macOS / Linux
```bash
export BROWSERSTACK_USERNAME="your_browserstack_username"
export BROWSERSTACK_ACCESS_KEY="your_browserstack_access_key"
```

### ✅ Verify credentials
```bash
echo %BROWSERSTACK_USERNAME%   # Windows
echo $BROWSERSTACK_USERNAME    # macOS / Linux
```

---

## 🚀 How to Run the Test

Make sure you are in the project root directory:

```bash
python tests/test_login2.py
```

---

## 🧠 What Happens When You Run It

- Selenium connects to BrowserStack using Remote WebDriver
- Test runs on a real Chrome browser (Windows 11)
- Login flow is executed automatically
- Assertion validates successful login
- BrowserStack records:
  - Test status
  - Browser & OS
  - Video recording
  - Logs

---

## ✅ Sample Output

```
✅ BrowserStack Login Test Passed
```

### BrowserStack Dashboard
- Browser: Chrome
- OS: Windows 11
- Status: PASSED
- Video recording available

---

## 🔐 Security Best Practices Followed

```python
if not BROWSERSTACK_USERNAME or not BROWSERSTACK_ACCESS_KEY:
    raise Exception("BrowserStack credentials not set in environment variables")
```

---

## 🧪 Test Logic Overview

### browserstack_config.py
- Reads credentials from environment variables
- Defines browser and OS capabilities
- Initializes Selenium Remote WebDriver

### test_login2.py
- Imports shared driver configuration
- Performs login automation
- Validates successful authentication
- Closes browser session cleanly

---

## 🎤 Interview Explanation

“I built a Selenium-based automation framework where I first validated tests locally and then executed the same scripts on BrowserStack’s real cloud browsers. This allowed me to test cross-browser compatibility without changing the core test logic.”

---

## 📄 Resume Bullet Points

- Built an end-to-end UI automation framework using Selenium WebDriver with Python  
- Executed automated test cases across real browsers and operating systems using BrowserStack Cloud  
- Designed reusable test configurations enabling cross-browser execution  
- Secured sensitive credentials using environment variables  
- Documented setup and execution steps in GitHub README  

---

## 🚧 Future Enhancements

- Convert framework to pytest
- Add parallel execution
- Integrate GitHub Actions CI/CD
- Extend coverage to form submission and API validation

---

## 👤 Author

**Kshitij Jadhav**  
Budding Engineer  
Mumbai, India

---

⭐ If you like this project, give it a ⭐ on GitHub!
