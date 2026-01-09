"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Rohan Gadade',
    'title': 'Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'rohangadade24@gmail.com',
    'github': 'https://github.com/rohan2-4',
    'linkedin': 'https://www.linkedin.com/in/rohan-gadade-bb05aa2a7/',
}

SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 75},
    {'name': 'Flask', 'level': 60},
    {'name': 'Git', 'level': 70},
    {'name':'Java', 'level': 65},
    {'name':'C', 'level': 60},
    {'name':'power bi', 'level': 55},
    {'name': 'JavaScript', 'level': 50},
    {'name': 'SQL', 'level': 45},
    {'name':'DBMS', 'level': 50},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Todo App', 'description': 'A simple task management application.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 3, 'name': 'Weather Dashboard', 'description': 'Display weather data from an API.', 'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},
    {'id': 4, 'name': 'poll and survey Telegram bot', 'description': 'A telegram bot to create polls and surveys', 'tech': ['Python', 'Flask', 'Telegram Bot API'], 'status': 'Completed'},
    {'id': 5, 'name': 'Campuslinker', 'description': 'A platform for the student can fill admission form,exam,result,social activity.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'completed'}
]   
BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Getting Started with Flask',
        'date': '2024-01-15',
        'author': 'Rohan Gadade',
        'excerpt': 'Flask is an amazing micro web framework for Python. Here\'s how I got started...',
        'content': 'Flask has been an incredible journey for me. Starting with the basics of routing and templates, I quickly learned how powerful and flexible this framework is. The simplicity of Flask makes it perfect for beginners, yet it\'s powerful enough for complex applications.',
        'tags': ['Flask', 'Python', 'Web Development']
    },
    {
        'id': 2,
        'title': 'Building RESTful APIs',
        'date': '2024-01-20',
        'author': 'Rohan Gadade',
        'excerpt': 'Learn how to create clean and efficient REST APIs using Flask...',
        'content': 'RESTful APIs are the backbone of modern web applications. In this post, I explore how Flask makes it easy to create APIs with clean routes, proper HTTP methods, and JSON responses. Understanding REST principles is crucial for any web developer.',
        'tags': ['API', 'Flask', 'REST']
    },
    {
        'id': 3,
        'title': 'Database Integration with Flask',
        'date': '2024-01-25',
        'author': 'Rohan Gadade',
        'excerpt': 'Connecting Flask to databases using SQLAlchemy and SQLite...',
        'content': 'Working with databases is essential for dynamic web applications. I\'ve been exploring Flask-SQLAlchemy, which provides a wonderful ORM for database operations. SQLite is perfect for development, and migrating to PostgreSQL for production is straightforward.',
        'tags': ['Database', 'SQLAlchemy', 'Flask']
    },
    {
        'id': 4,
        'title': 'Deploying Flask Applications',
        'date': '2024-02-01',
        'author': 'Rohan Gadade',
        'excerpt': 'A guide to deploying your Flask app to production...',
        'content': 'Taking your Flask app from development to production requires understanding deployment strategies. I cover various options including Heroku, AWS, and DigitalOcean. Each platform has its advantages, and choosing the right one depends on your project needs.',
        'tags': ['Deployment', 'DevOps', 'Flask']
    }
]




# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break

    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)
@app.route('/blog')
def blog():
    return render_template('blog.html', info=PERSONAL_INFO, posts=BLOG_POSTS)


@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = None
    for p in BLOG_POSTS:
        if p['id'] == post_id:
            post = p
            break
    return render_template('blog_post.html', info=PERSONAL_INFO, post=post, post_id=post_id)

@app.route('/skill/<skill_name>')
def skill_detail(skill_name):
    # Find the skill
    skill = None
    for s in SKILLS:
        if s['name'].lower() == skill_name.lower():
            skill = s
            break
    
    # Find projects that use this skill
    related_projects = []
    if skill:
        for project in PROJECTS:
            for tech in project['tech']:
                if tech.lower() == skill_name.lower():
                    related_projects.append(project)
                    break
    
    return render_template('skill_detail.html', 
                         info=PERSONAL_INFO, 
                         skill=skill, 
                         skill_name=skill_name,
                         related_projects=related_projects)

@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
