# Django Blog Project

A simple Blog Web Application built with Django.

This project was created to practice Django fundamentals including Models, Migrations, Django Admin, Class-Based Views, URL Routing, Dynamic URLs, Templates, Django Template Language (DTL), Search, Sorting, Image Uploads, Active/Inactive Blog Filtering, and User Authentication.

---

## Project Requirements

The project was developed with the following requirements:

- Use a single Blog model
- Model fields:
  - Title
  - Description
  - Created At
  - Image
  - Is Active
- Create two pages:
  1. Blog List Page
  2. Blog Detail Page
- Blog List Page should display active blogs
- Each blog should have a link to its detail page
- Blog Detail Page should display the complete details of the selected blog
- Add search functionality
- Add sorting functionality
- Use Class-Based Views
- Create an accounts app
- Implement user signup
- Implement user login
- Implement user logout

---

## Features

- Single `Blog` model
- Create and manage blogs using Django Admin
- Blog title and description
- Blog creation date
- Blog image upload
- Active/Inactive blog status
- Only active blogs are displayed on the blog list page
- Dynamic detail page for each blog
- Search blogs by title
- Sort blogs by newest or oldest
- Search and sorting can be used together
- Class-Based View for the blog list
- Django Generic `DetailView` for the blog detail
- Back to Blogs navigation link
- Support for HTML content in trusted blog descriptions
- User signup
- User login
- User logout
- Django built-in authentication
- Authentication using Class-Based Views
- Login redirects users to the blog list
- Logout redirects users to the login page

---

## Search Filter

The blog list page includes a search filter.

Users can search for blogs by entering a keyword in the search field.

The search uses Django ORM's `icontains` lookup to perform a case-insensitive title search.

Example:

/blogs/?search=Python

---

## Sorting Filter

The blog list page includes sorting options:

- Newest First
- Oldest First

The sorting is performed using Django ORM's `order_by()` method.

Examples:

/blogs/?sort=newest

/blogs/?sort=oldest

---

## Search and Sorting Together

Search and sorting can be used together.

Example:

/blogs/?search=Django&sort=newest

This filters blogs by the search keyword and then sorts the results.

---

## Image Upload

The Blog model uses Django's `ImageField` for blog images.

```python
image = models.ImageField(
    upload_to="blogs/",
    blank=True,
    null=True
)

---

##Project Structure
django_blog_test/
│
├── accounts/
│   ├── templates/
│   │   └── accounts/
│   │       ├── signup.html
│   │       └── login.html
│   ├── forms.py
│   ├── urls.py
│   └── views.py
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── blog_list.html
│   │       └── blog_detail.html
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── media/
├── manage.py
└── README.md



