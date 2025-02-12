from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.


def home(request):
    return render(request, "home/index.html", {"page_title": "Home"})

def projects(request):
    return render(request, "home/projects.html" , {"page_title": "Projects"})

def resources(request):
    tools_posts = Post.objects.filter(categories__name="tools")
    guides_posts = Post.objects.filter(categories__name="guides")

    return render(request, "home/resources.html", {
        "page_title": "Resources",
        "tools_posts": tools_posts,
        "guides_posts": guides_posts,
    })

def writeups(request):
    # Fetch posts based on their categories
    ctf_posts = Post.objects.filter(categories__name="CTF")
    thm_posts = Post.objects.filter(categories__name="THM")
    hackerone_posts = Post.objects.filter(categories__name="HackerOne")
    vulnhub_posts = Post.objects.filter(categories__name="VulnHub")

    return render(request, "home/writeups.html", {
        "page_title": "Writeups",
        "ctf_posts": ctf_posts,
        "thm_posts": thm_posts,
        "hackerone_posts": hackerone_posts,
        "vulnhub_posts": vulnhub_posts
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.categories.filter(name__iexact="writeup").exists():
        template_name = "home/writeup_detail.html"
    elif post.categories.filter(name__iexact="resources").exists():
        template_name = "home/resources_detail.html"
    else:
        # Optional: Handle case where the post doesn't belong to a known category
        template_name = "home/unknown_detail.html"
        
    return render(request, "home/post_detail.html", {
        "page_title": post.slug,
        "post": post,
    })
#def success_page(request):
 #   return HttpResponse("Hey this is success page")
