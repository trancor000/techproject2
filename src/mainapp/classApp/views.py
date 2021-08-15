from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ClassForm
from .models import djangoClasses




def admin_console(request):
    classes = djangoClasses.objects.all()
    return render(request, 'products/products_page.html', {'classes': classes})

# gives details about the classes added
def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(djangoClasses, pk=pk)
    form = ClassForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'products/present_product.html', {'form': form})

# allows for the deletion of any class
def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(djangoClasses, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    context = {"item": item, }
    return render(request, "classes/confirmDelete.html", context)

# asks for confirmation with the deletion request
def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = djangoClasses(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console')
    else:
        return redirect('admin_console')


def createRecord(request):
    form = ClassForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        form = ClassForm()
    context = {
        'form': form,
    }
    return render(request, 'classes/createRecord.html', context)
