# Automated-Vehicle-Insurance-Claim-Evaluation-System

InsureIQ automates vehicle insurance claims by replacing manual damage surveys with a CNN-based image classifier. Agents submit accident photos via an Android app, the system predicts damage severity and an estimated payout, and an admin web portal handles policy management and claim approvals.

> Final-year B.Tech project, Dept. of CSE, College of Engineering Kidangoor (APJ Abdul Kalam Technological University), June 2023.
> Published: [IRJMETS Vol. 5](https://www.doi.org/10.56726/IRJMETS40598)

## Features

**Admin (Web Portal):** manage policies (CRUD), approve/reject policy and damage claims, reply to complaints.

**Agent (Android App):** register/login, browse policies, request a new policy, submit a damage claim with photos, track claim/policy status, file complaints.

## Tech Stack

- **Backend:** Python, Flask
- **ML:** TensorFlow, Keras, OpenCV
- **Database:** MySQL
- **Frontend:** HTML/CSS/JS (Jinja templates)
- **Mobile:** Android (Java)

## Project Structure
├── main.py # Flask entry point

├── public.py # Public routes (home, login)

├── admin.py # Admin routes (policies, claims, complaints)

├── api.py # REST API consumed by the Android app

├── database.py # MySQL query helpers

├── cnn.py # CNN training script

├── newcnn.py # CNN inference (used by api.py)

├── model1.h5 # Trained CNN weights

└── android-app/ # Android client

## Setup

```bash
git clone https://github.com/<your-username>/InsureIQ.git
cd InsureIQ
pip install flask flask_mail mysql-connector-python tensorflow keras opencv-python numpy scikit-learn

# Create the DB and set credentials in database.py
mysql -u root -p -e "CREATE DATABASE insurance_prediction"

python main.py   # runs on http://localhost:5073
```

For the Android app: open `android-app/` in Android Studio, point it at your running API URL, and build.

## API Overview

| Endpoint | Description |
|---|---|
| `/api/reg`, `/api/logins` | Agent registration & login |
| `/api/agent_view_policy` | List policies |
| `/api/agent_request_policy` | Request a policy |
| `/api/agent_damage_request/` | Submit claim photos → get predicted damage class & payout |
| `/api/agent_send_complaint` | Submit a complaint |

## Results

CNN damage classifier achieved **63% validation accuracy**. Damage class, vehicle age, and odometer reading were the strongest predictors of claim amount.

## Contributors

Ajeesh Alan · Ajesh S · Kashinath S · Siddhharth B

**Guide:** Mrs. Rakhi Ramachandran Nair, Dept. of CSE, CE Kidangoor
