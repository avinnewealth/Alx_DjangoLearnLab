## Authentication System

This project uses Django’s built-in authentication framework.

### Features
- User registration
- User login and logout
- Profile viewing and editing

### How It Works
- Django authentication views handle login/logout
- Custom views handle registration and profile updates
- CSRF protection is enabled on all forms

### Testing
1. Run `python manage.py runserver`
2. Visit `/register` to create an account
3. Login at `/login`
4. Access profile at `/profile`

## Blog Post Management (CRUD)

### Features
- View all blog posts
- View individual posts
- Create new posts (authenticated users only)
- Edit and delete posts (author only)

### Permissions
- Only logged-in users can create posts
- Only post authors can edit or delete their posts

### URLs
- /posts/ – list all posts
- /posts/new/ – create post
- /posts/<id>/ – view post
- /posts/<id>/edit/ – edit post
- /posts/<id>/delete/ – delete post
