# Document Scanner System

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
git clone <repository-url>
cd backend
