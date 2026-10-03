# Django Blog Project

A simple Blog Web Application built with Django.

This project was created to practice Django fundamentals including Models, Migrations, Django Admin, Function-Based Views, Class-Based Views, URL Routing, Dynamic URLs, Templates, Django Template Language (DTL), Template Filters, Search Filtering, and Sorting.

---

## Project Requirements

The project was developed with the following requirements:

- Use a single model
- Model fields:
  - Title
  - Description
  - Created At
- Create two pages:
  1. Blog List Page
  2. Blog Detail Page
- Blog List Page should display all blogs with their titles
- Each blog should have a link to its detail page
- Blog Detail Page should display the complete details of the selected blog
- Add a search filter for blogs
- Add a sorting filter for blogs
- Learn and implement Class-Based Views (CBV)

---

## Features

- Single `Blog` model
- Create and manage blogs using Django Admin
- Display all blogs on the list page
- Display blog titles and short descriptions
- Dynamic detail page for each blog
- Display complete blog description
- Display blog creation date
- Back to Blogs navigation link
- Support for HTML headings, bullet lists, and numbered lists in trusted blog content
- Search blogs by title
- Sort blogs by newest or oldest
- Use search and sorting filters together
- Class-Based View (CBV) for the blog list page

---

## Technologies Used

- Python
- Django
- SQLite
- HTML
- Django Template Language (DTL)

---

## Search Filter

The Blog List Page includes a search filter that allows users to search blogs by title.

The search uses Django ORM's `icontains` lookup, which performs a case-insensitive partial match.

Example:

```text
/blogs/?search=Python
