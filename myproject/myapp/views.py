# Create your views here.
from django.shortcuts import render

"""
from django.views.generic import TemplateView
from templates.forms import HomeForm

class HomeView(TemplateView):
    template_name = 'templates/contact.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('contact: contact')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
"""


def index(request):
    return render (request, 'index.html')

def contact (request):
    return render (request, 'contact.html')

def gallery (request):
    return render (request, 'gallery.html')

def programs (request):
    return render (request, 'programs.html')

def about (request):
    return render (request, 'about.html')

def products (request):
    return render (request, 'products.html')


"""
def submit (request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        description = request.POST['company']
        if form.is_valid():
            form.save()
            # assert false
            send_mail('Contact Form', description, settings.EMAIL_HOST_USER, ['dmitrybozhko@mail.ru'], fail_silently=False)
            return HttpResponseRedirect('/contact/?submitted=True')
    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'contact.html', {'form': form, 'page_list': Page.objects.all(), 'submitted'})
"""
"""

def questions(request):
    questions = Question.objects.order_by('date_added')
    context = {'questions': questions}
    return render(request, 'questions.html', context)

def question(request, question_id):
    #Выводит одну тему и все ее записи.
    question = Question.objects.get(id=question_id)
    answers = question.answer_set.order_by('-date_added')
    context = {'question': question, 'answers': answers}
    return render(request, 'question.html', context)

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)

def topic(request, topic_id):
    #Выводит одну тему и все ее записи.
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)
"""
