# FixMyStreet 🛣️📸

**FixMyStreet** is a civic issue reporting platform that allows citizens to capture and upload images of local problems such as potholes, broken street lights, and garbage. These reports can then be viewed by local authorities, helping them identify, track, and resolve issues efficiently.

The project is built using **Django Rest Framework** and focuses on secure, scalable APIs for real-world problem reporting.

---

## 🚀 Features

- 📸 **Image-based issue reporting**
  - Upload photos of street problems such as potholes, garbage, or broken lights.
- 📍 **Location-aware reporting**
  - Issues are associated with specific locations for easier tracking.
- 🔐 **Authentication & Authorization**
  - User authentication powered by **Djoser**.
  - Custom permissions implemented to secure API endpoints.
- ☁️ **Cloud Image Storage**
  - Images are stored securely using **Cloudinary**.
- 🛠️ **RESTful API**
  - Fully API-driven backend built with Django Rest Framework.
- 🏛️ **Government-friendly workflow**
  - Designed so local authorities can review and act on reported issues.

---

## 🧰 Tech Stack

| Layer        | Technology |
|--------------|------------|
| Backend      | Django, Django Rest Framework |
| Authentication | Djoser |
| Image Storage | Cloudinary |
| Database     | SQLite  |
| Security     | Custom DRF Permissions |
| API Format   | JSON |

---

## 📦 Installation & Setup

Follow these steps to run the project locally:

### 1️ Clone the Repository

```bash
git clone https://github.com/Mr-AshishBhandari/FixMyStreet.git
cd FixMyStreet
```

### 2 Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3 Install Dependencies
```bash
pip install -r requirements.txt
```
### 4 Environment Variables
```bash
# create a .env file and add the following

SECRET_KEY=your_django_secret_key
DEBUG=True

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```
### 5 Apply Migrations
``` bash
python manage.py makemigrations
python manage.py migrate
```
### 6 Run the Server
``` bash
python manage.py runserver
```

Visit the API at:
```bash
http://127.0.0.1:8000/
```




