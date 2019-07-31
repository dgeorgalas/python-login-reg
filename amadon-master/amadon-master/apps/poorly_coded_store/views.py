from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def end(request):
    # if request.method == "GET":
    #     total_charge = quantity_from_form * price_from_form
    #     print("Charging credit card $" + str(total_charge))
    #     Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    orders = Order.objects.all()
    last_order = Order.objects.last()

    sum = 0
    for order in orders:
        sum += (order.total_price)
    all = 0
    for order in orders:
        all += (order.quantity_ordered)
    context = {
        "sum" : sum,
        "all" : all,
        "last_order" : last_order
    }
    # orders = Order.objects.all()
    # sum = 0
    # for order in orders:
    #     sum += (order.total_price)
    # sum_quantity = 0
    # for order in orders:
    #     sum_quantity += (order.quantity_ordered)
    # context = {
    #     "quantity_from_form": quantity_from_form,
    #     "total_charge": total_charge,
    #     "sum" : sum,
    #     "sum_quantity" : sum_quantity
    # }
    return render(request, "store/checkout.html", context)

def checkout(request):

    quantity_from_form = int(request.POST["quantity"])
    product_id_from_form = float(request.POST["product_id"])
    price_from_form = Product.objects.get(id=product_id_from_form)
    total_charge = quantity_from_form * price_from_form.price
    print("Charging credit card $" + str(total_charge))
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    # orders = Order.objects.all()
    # sum = 0
    # for order in orders:
    #     sum += (order.total_price)
    # sum_quantity = 0
    # for order in orders:
    #     sum_quantity += (order.quantity_ordered)
    # context = {
    #     "quantity_from_form": quantity_from_form,
    #     "total_charge": total_charge,
    #     "sum" : sum,
    #     "sum_quantity" : sum_quantity
    # }
    return redirect( "/end")