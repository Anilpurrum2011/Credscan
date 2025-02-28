# Credscan

A self-contained document scanning and matching system with a built-in credit system. Users can upload documents, scan them for matches, and manage their credits. Admins can approve credit requests and view analytics.

---

## Features

1. **User Authentication:**
   - User registration and login.
   - Profile page to view credits and past scans.

2. **Credit System:**
   - Each user gets 20 free credits per day (auto-reset at midnight).
   - Users can request additional credits, which require admin approval.

3. **Document Scanning & Matching:**
   - Users can upload plain text files for scanning.
   - The system compares uploaded documents with existing documents using a text similarity algorithm.
   - Displays matching documents with similarity scores.

4. **Admin Dashboard:**
   - Admins can approve or deny credit requests.
   - Admins can view analytics, including:
     - Total number of users.
     - Total number of scans.
     - Top users by scans.
     - Total credit usage.

5. **Smart Analytics:**
   - Track user activity, scans, and credit usage.
   - Generate reports for admins.

---

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **File Storage:** Local file storage for uploaded documents
- **Text Matching:** Difflib (basic text similarity algorithm)

---

## Setup Instructions

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Anilpurrum2011/Credscan.git
cd backend

### 1. Install Dependencies
Ensure you have Python installed. Then, install the required dependencies:

```bash
pip install django
```

### 2. Run Migrations
Set up the database by running migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create a Superuser (Admin)
Create an admin account to access the admin dashboard:

```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

### 4. Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```
The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage Instructions

### 1. Register and Log In
- Register at [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)
- Log in at [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

### 2. Upload Documents
- After logging in, go to the profile page: [http://127.0.0.1:8000/profile/](http://127.0.0.1:8000/profile/)
- Click "Upload Document" to upload a plain text file (.txt).
- The system will deduct 1 credit and display matching documents.

### 3. Request Additional Credits
- If you run out of credits, click "Request More Credits" on the profile page.
- Admins can approve or deny your request.

### 4. Admin Dashboard
- Log in as an admin user.
- Visit the admin dashboard: [http://127.0.0.1:8000/admin/dashboard/](http://127.0.0.1:8000/admin/dashboard/)
- Approve or deny credit requests.
- View analytics at: [http://127.0.0.1:8000/admin/analytics/](http://127.0.0.1:8000/admin/analytics/)

## Project Structure

```
backend/
├── manage.py
├── backend/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── scanner/
│   ├── migrations/
│   ├── templates/
│   │   └── scanner/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── profile.html
│   │       ├── upload.html
│   │       ├── matches.html
│   │       ├── request_credits.html
│   │       ├── admin_dashboard.html
│   │       └── admin_analytics.html
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── scripts.js
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── media/
│   └── documents/  # Uploaded documents are stored here
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | /auth/register/ | User registration |
| POST | /auth/login/ | User login |
| GET | /user/profile/ | Get user profile and credits |
| POST | /scan/ | Upload document for scanning |
| GET | /matches/<int:docId>/ | Get matching documents |
| POST | /credits/request/ | Request additional credits |
| GET | /admin/dashboard/ | Admin dashboard for credit requests |
| GET | /admin/analytics/ | Admin analytics dashboard |

## Screenshots
(Add screenshots in the `screenshots/` folder and update paths here)

- **Home Page**   ![WhatsApp Image 2025-02-28 at 15 51 21_cfdebe6b](https://github.com/user-attachments/assets/50ab1d55-22ca-43d1-baff-9c7ee1ad3f87)

- **Login Page**  ![WhatsApp Image 2025-02-28 at 15 51 40_4d3920b6](https://github.com/user-attachments/assets/ac72c17c-2470-4291-a0e7-bf5567d5d9b9)

- **Profile Page**  ![WhatsApp Image 2025-02-28 at 15 52 04_45c71d3c](https://github.com/user-attachments/assets/a6fa8865-1782-4903-ba36-4fc208a46d7b)

- **Upload Document**  ![WhatsApp Image 2025-02-28 at 15 52 54_4e484351](https://github.com/user-attachments/assets/67b14d0c-dddb-4e3d-9efa-d7eaceeb30e5)

- **Request Additional Credits**  ![WhatsApp Image 2025-02-28 at 15 52 30_56f2ae96](https://github.com/user-attachments/assets/7d798ad7-ae0c-4a60-8af8-2e6ed06d92f5)


## Contributing

Contributions are welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or feedback, contact:

- **Your Name**
- **Email:** anilpurrum@gmail.com
- **GitHub:** https://github.com/Anilpurrum2011/

---



