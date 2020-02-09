from django.shortcuts import render

posts = [
    {
        'author': 'AlfonsoMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 27, 2020'
    },
    {
        'author': 'AlfonsoMS',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 28, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
