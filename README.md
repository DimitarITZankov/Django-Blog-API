# Django Blog API

A RESTful API for a blog platform built with **Django** and **Django REST Framework** (DRF).  
Supports **user registration**, **token-based authentication**, and basic blog management features.

---

## Features

- **Custom User Model** (`BlogAPIProfiles`)  
  - Username, first name, last name, email, password  
  - Passwords are hashed automatically  
- **User Registration API** (`/api/register/`)  
- **Token-based Login API** (`/api/login/`)  
- **Blog Post Management** (future expansion)  
- **DRF ViewSets and Routers** for clean URL structure  
- Secure password handling and authentication  

---

## Tech Stack

- **Backend:** Django 2.2, Django REST Framework  
- **Authentication:** DRF Token Authentication  
- **Database:** SQLite (default, can be switched to PostgreSQL)  
- **Environment Management:** Python virtualenv, Vagrant setup supported  

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/DimitarITZankov/Django-Blog-API.git
cd Django-Blog-API
---
### 2. Create virtual environment
