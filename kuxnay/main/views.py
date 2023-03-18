from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import authorizationForm, loginForm
from .models import Recipes, Tags , IpModel
from django.views.generic import DetailView, CreateView
from django.views.generic import ListView

from .utils import DataMixin


class indexpage(ListView):
    paginate_by = 3
    model = Recipes
    template_name = 'main/index.html'
    context_object_name = 'recipesmini'

class mostview(ListView):
    template_name = 'main/mostviews.html'
    context_object_name = 'recipesmini'

    def get(self, request, *args, **kwargs):
        popular = Recipes.objects.order_by(
            '-views')[:1]

        context['recipesmini'] = popular

        return self.render_to_response(context)


class recipedetail(DetailView):
    model = Recipes
    context_object_name = 'recipe'
    template_name = 'main/recipe.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        ip = get_client_ip(self.request)
        print(ip)
        if IpModel.objects.filter(ip=ip).exists():
            print("ip already present")
            post_id = request.GET.get('post-id')
            print(post_id)
            recipe = Recipes.objects.get(pk=post_id)
            recipe.views.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            post_id = request.GET.get('post-id')
            recipe = Recipes.objects.get(pk=post_id)
            recipe.views.add(IpModel.objects.get(ip=ip))
        return self.render_to_response(context)


class categories(ListView):
    paginate_by = 9
    model = Tags
    template_name = 'main/categories.html'
    context_object_name = 'Tags'



def accounts(request):
    return render(request, 'main/accounts.html')


def createuser(request):
    if request.method == 'POST':
        form = authorizationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        authorizationForm()


class authorization(DataMixin, CreateView):
    form_class = authorizationForm
    template_name = 'main/authorization.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class login(DataMixin, LoginView):
    form_class = loginForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Вход")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logoutuser(request):
    logout(request)
    return redirect('login')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARD_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return  ip

