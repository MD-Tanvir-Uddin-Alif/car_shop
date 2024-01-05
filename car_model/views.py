from django.shortcuts import render, redirect
from django.views.generic import DetailView
from . import models
from . import forms
# Create your views here.

class detailiView(DetailView):
    model = models.Car_Model
    pk_url_kwarg = 'id'
    template_name = 'car_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

def buy_view(request, id):
    if request.method == 'POST':
        car_model = models.Car_Model.objects.get(id=id)
        user = request.user
        if car_model.quantity > 0:
            buy = models.BuyModel.objects.create(car=car_model, buyer=user)
            car_model.quantity -= 1
            car_model.save()
            
            return redirect('profile_page')

    return render(request, 'profile.html')

# def User_Buying_details(request):
#     user = request.user
#     details = models.BuyModel.objects.filter(buyer=user)
#     return render(request,'profile.html',{'details':details})