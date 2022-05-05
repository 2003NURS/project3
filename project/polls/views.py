from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import  settings

# from django.http import HttpResponse
# from django.utils.translation import ugettext as _

# def send_message(request):
#     send_mail("Welcome to testing page", "My content", "200103263@stu.sdu.edu.kz",
#               ["aeigeriiim@gmail.com", "200103263@stu.sdu.edu.kz"],
#               fail_silently=False, html_message="<b>Bold text </b> <i>Italic text </i>")
#
#     return render(request, 'polls/successfull.html')


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})


def index(request):
    posts = Posts.objects.all
    return render(request, 'polls/index.html', {'posts': posts})
    output = _('StatusMsg')
    return HttpResponse(output)


def show_post(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
    context = {'post': post}
    return render(request, 'polls/post.html', context=context)


#
# def registration(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = AddPostForm()
#     return render(request, 'polls/registration.html',{'form': form,'title': 'registration'})
def registration(request):
    # form = AddPostForm()
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            # Registration.objects.create(**form.cleaned_data)
            return redirect('login')
    else:
        form = AddPostForm()
    return render(request, 'polls/registration.html', {'title': 'Мақаланы қосу', 'form': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'polls/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_user_context(title="Login")
        return dict(list(context.items()))

    def get_user_context(self, title):
        pass

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')


class RegisterUser(CreateView):
    form_class = AddPostForm
    template_name = 'polls/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_user_context(title='Registration')
        return dict(list(context.items()))

    def get_user_context(self, title):
        pass


def register_done(request):
    new = Registration.objects.order_by('-id')[:1]
    return render(request, 'polls/index.html', {'news': new})


class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'polls/send_message.html'

    def get(self, request):
        form = self.form_class()
        return render(request, 'polls/send_message.html', {'email_form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, 'polls/send_message.html',
                              {'email_form': form,
                               'error_message': 'Электрондық пошта мекенжайына жіберілді %s' % email})
            except:
                return render(request, 'polls/send_message.html',
                              {'email_form': form, 'error_message': 'Не тіркеме тым үлкен немесе бүлінген'})

        return render(request, 'polls/send_message.html',
                      {'email_form': form,
                       'error_message': 'Электрондық поштаны жіберу мүмкін емес. Тағы жасауды сәл кейінірек көріңізді өтінеміз'})



def deathNote(request):
    return render(request,'polls/deathNote.html')





def home(request):
    return render(request,'polls/home.html')


def services(request):
    return render(request,'polls/services.html')


def gallery(request):
    return render(request,'polls/gallery.html')


def demonSlashingBlade(request):
    return render(request,'polls/demonSlashingBlade.html')


def aboutMe(request):
    return render(request,'polls/aboutMe.html')


def contact(request, contactUser=None):
    form_class = contactUser
    error = ""
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['email']
        s = request.POST['subject']
        m = request.POST['message']
        try:
            Contact.objects.create(name=n, contact=c, email=e, subject=s, message=m, msgdate=date.today(), isread="no")
            error = "no"
        except:
            error = "yes"
    return render(request, 'polls/send_message.html', locals())