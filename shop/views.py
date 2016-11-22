from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.views.generic import ListView, DetailView
from models import Product

class ProductListView(ListView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ProductDetailView(DetailView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# class ProductEditView(DetailView):
#
#     model = Product
#
#     def post_edit(request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         if request.method == "POST":
#            form = PostForm(request.POST, instance=post)
#            if form.is_valid():
#               post = form.save(commit=False)
#               post.author = request.user
#               post.published_date = timezone.now()
#               post.save()
#               return redirect('post_detail', pk=post.pk)
#         else:
#              form = PostForm(instance=post)
#              return render(request, 'blog/post_edit.html', {'form': form})
