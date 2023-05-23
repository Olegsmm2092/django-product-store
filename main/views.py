from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Product, Customer
from .forms import CustomerForm


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.order_by('product_name')
    template_name = 'main/product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    fields = ['product_name', 'product_price', 'product_size']
    # fields = "__all__"
    template_name = 'main/product_create.html'
    # success_url = "/products/"
    success_url = reverse_lazy('main:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    success_url = reverse_lazy('main:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    # fields = ['product_name', 'product_price', 'product_size']
    fields = "__all__"
    template_name = 'main/product_update.html'
    success_url = reverse_lazy('main:product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'


class CustomerListView(ListView):
    model = Customer
    template_name = 'main/customer_list.html'
    context_object_name = 'customers'


class CustomerCreateView(CreateView):
    model = Customer
    # form_class = CustomerForm
    template_name = 'main/customer_create.html'
    fields = '__all__'
    success_url = reverse_lazy('main:customer_list')

    def form_valid(self, form=CustomerForm):
        # Save the customer instance to the database
        form.save()
        return super().form_valid(form)


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'main/customer_detail.html'
    context_object_name = 'customer'


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'main/customer_update.html'
    fields = '__all__'
    context_object_name = 'customer'
    success_url = reverse_lazy('main:customer_list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'main/customer_confirm_delete.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('main:customer_list')


class CustomerProductDetailView(DetailView):
    model = Customer
    template_name = 'main/customer_product_detail.html'
    context_object_name = 'customer'
