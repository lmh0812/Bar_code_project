from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.http import Http404
# from django.template import loader
from .forms import PostForm, UploadForm, Post2Form
from django.utils import timezone

from main.models import Question, Bar_code, Img, Imgadd
from .bar_read import bar_read
from django.conf import settings

# Create your views here.

# def home(request):
#     return render(request, 'main/home.html')
# def product(request):
#     return render(request, 'main/product.html')
# def insert(request):
#     return render(request, 'mian/insert.html')

def home(request):
    code_list = Bar_code.objects.all()
    # if code_id is not None:
    #     code = get_object_or_404(Bar_code, pk=code_id)
    #     return render(request, 'main/insert.html', {'code':code})
    return render(request, 'main/home.html', {'code_list':code_list})

# def ins(request, code_id):
#     # if code_id is not None:
#     code = get_object_or_404(Bar_code, pk=code_id)
#     return render(request, 'main/home/ins.html', {'code':code})
#     # return HttpResponseRedirect('/main/home/')
#     # return render(request, 'main/home/insert.html')

def ins(request):
    return render(request, 'main/ins.html')

# def add(request, code_id):
#     code = get_object_or_404(Bar_code, pk=code_id)
#     try:
#         selected_code = code.objects.get(pk=request.POST['add'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'main/detail.html', {
#             'code': code,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_code.votes += 1
#         selected_code.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('main:results', args=(code.id,)))

# def add(request):
#     if request.method == 'POST':
#         Bar_code(
#             code = request.POST.get('code'),
#             name = request.POST.get('name'),
#             charge = request.POST.get('charge'),
#         ).save()
#     return HttpResponseRedirect('/main/home')

# def add(request, code_id):
#     code = get_object_or_404(Bar_code, pk=code_id)
#     try:
#         add_code = code.choice_set.get(pk=request.POST['code'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'main/home.html', {
#             'code': code,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         add_code.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('main:home', args=(code.id,)))


def add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/main/home')
    else:
        form = PostForm()
    return render(request, 'main/add.html', {'form': form})

def post_detail(request, code_id): # code_id 가져오기
    post = get_object_or_404(Bar_code, pk=code_id)
    return render(request, 'main/post_detail.html', {'post': post})

def post_edit(request, code_id):
    post = get_object_or_404(Bar_code, pk=code_id) # post.id로 입력해야함 post_detail.html에서
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/main/home')
    else:
        form = PostForm(instance=post)
    return render(request, 'main/add.html', {'form': form})

def post_delete(request, code_id):
    post = Bar_code.objects.get(id=code_id)
    post.delete()
    return redirect('/main/home')

def upload_image(request):
    img_list = Img.objects.all()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            imageURL = settings.MEDIA_URL + form.instance.image.name
            bar_read(settings.MEDIA_ROOT_URL + imageURL)
            return redirect('/main/upload')
    else:
        form = UploadForm()
    return render(request, 'main/upload.html', {'form':form, 'img_list':img_list})

def img_detail(request, img_id):
    post = get_object_or_404(Img, pk=img_id)
    result = bar_read(post.image.path)
    return render(request, 'main/img_detail.html', {'post':post, 'result':result})

def img_add(request):
    img_list = Img.objects.all()
    if request.method == 'POST':
        form = Post2Form(request.POST, request.FILES)
        if form.is_valid():
            imageURL = settings.MEDIA_URL + form.instance.image.name
            post.code = bar_read(settings.MEDIA_ROOT_URL + imageURL)
            post.save()
            form.save()
            return redirect('/main/home')
    else:
        form = Post2Form()
    return render(request, 'main/img_add.html', {'form':form, 'img_list':img_list})






def index(request):
    # return HttpResponse("Hello, world.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5] # Question 데이터 중에서 출판일자를 정렬하여 5개까지만 데이터 가져오기
    # output = ', '.join([q.question_text for q in latest_question_list]) # 그리고 이 다섯개 데이터를 ,로 연결하겠다
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'main/index.html', context) 

def detail(request, question_id):
    # return HttpResponse("you're looking at question %s." % question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'main/detail.html', {'question':question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'main/detail.html', {'question':question})

def results(request, question_id):
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'main/results.html', {'question': question})

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'main/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('main:results', args=(question.id,)))