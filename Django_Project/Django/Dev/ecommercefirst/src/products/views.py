# from django.views import ListView
from django.views.generic import ListView, DetailView

from django.shortcuts import render,get_object_or_404
from django.http import Http404
# Create your views here.

from carts.models import Cart

from .models import Product

#class based view
class ProductFeaturedListView(ListView):
	
	template_name='products/list.html'

	def  get_queryset(self,*args,**kwargs):
		request = self.request
		return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
	"""docstring for ProductListView"""
	queryset=Product.objects.all().featured()

	template_name='products/featured-detail.html'

	# def  get_queryset(self,*args,**kwargs):
	# 	request = self.request
	# 	return Product.objects.featured()




class ProductListView(ListView):
	"""docstring for ProductListView"""
	queryset=Product.objects.all()
	template_name='products/list.html'

	# #by default,sends all quertset objects
	# def get_context_data(self,*args,**kwargs):
	# 	context=super(ProductListView,self).get_context_data(*args,**kwargs)
	# 	print(context)
	# 	return context
	def  get_queryset(self,*args,**kwargs):
		request = self.request
		return Product.objects.all()

#function based view
def product_list_view(request):
	queryset=Product.objects.all()
	context ={
		'object_list':queryset,
		"title":"Product Page",
	}
	return render(request,"products/list.html",context)


class ProductDetailSlugView(DetailView):
	queryset=Product.objects.all()
	template_name='products/detail.html'

	def get_context_data(self,*args,**kwargs):
		context = super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
		cart_obj,new_obj=Cart.objects.new_or_get(self.request)
		context['cart']=cart_obj
		return context

	def get_object(self,*args,**kwargs):
		request = self.request
		slug =self.kwargs.get("slug")
		# instance = get_object_or_404(Product,slug=slug,active=True)
		try:
			instance=Product.objects.get(slug=slug,active=True)

		except Product.DoesNotExist:
			raise Http404(" not found")
		except Product.MultipleObjectsReturned:
			qs=Product.objects.filter(slug=slug,active=True)
			instance = qs.first()
		except:
			raise Http404(" not found ummm!!")

		return instance
		




	#class based view
class ProductDetailView(DetailView):
	"""docstring for ProductListView"""
	queryset=Product.objects.all()
	template_name='products/detail.html'

	#by default,sends all quertset objects
	def get_context_data(self,*args,**kwargs):
		context=super(ProductDetailView,self).get_context_data(*args,**kwargs)
		print(context)
		# context['abc']=123
		return context

	def get_object(self,*args,**kwargs):
		request = self.request
		pk =self.kwargs.get("pk")
		instance = Product.objects.get_by_id(id=pk)
		if  instance== None:
			raise Http404("Product does not exists")
		return instance

	# def  get_queryset(self,*args,**kwargs):
	# 	request = self.request
	# 	pk =self.kwargs.get("pk")
	# 	return Product.objects.filter(pk=pk)

#function based view
def product_detail_view(request,pk=None,*args,**kwargs):
	# instance =Product.objects.get(pk=pk,featured=True)  #id
	# print(args)
	# print(kwargs)
	# instance =get_object_or_404(Product,pk=pk,featured=True)

	try:
		instance = Product.objects.get(id=pk)
	except Product.DoesNotExist:
		print("no product exists")
		raise Http404("Product does not exists")
	except:
		print("huh")

	instance = Product.objects.get_by_id(id=pk)
	if  instance== None:
		raise Http404("Product does not exists")


	# Issue with below 5 line code	 

	# qs = Product.objects.filter(id=pk)
	# print(qs)
	# if qs.exists() and qs.count==1:
	# 	instance=qs.first()
	# else:
	# 	raise Http404("Product does not exists")
	context ={
		'object':instance,
		"title":"Product Detail Page",
		# 'abc':123
	}
	return render(request,"products/detail.html",context)
