from django.shortcuts import render, redirect
from .models import cashFlow
from .forms import cashflowForm
from django.http import HttpResponse
from django.db.models import Sum
from .filters import CashFlowFilter

# Create your views here.
# Create your views here.
def home(request):
    cf_list = cashFlow.objects.all()
    cf_count = cashFlow.objects.count()
    if cf_count < 1:
        cf = cashFlow(price=0, desc='mulai baru', saldoCredit=0, tipe='Debit', saldoDebit=0)
        cf.save()
    agg_Credit = cashFlow.objects.aggregate(Sum('saldoCredit'))['saldoCredit__sum']
    agg_Debit = cashFlow.objects.aggregate(Sum('saldoDebit'))['saldoDebit__sum']

    last_saldo= agg_Debit-agg_Credit

    context = {
        'cf_list': cf_list,'last_saldo':last_saldo
    }
    return  render(request,'finance/home.html',context)


def add(request):
    #cf_list = cashFlow.objects.all()
    #last_saldo = cf_list.last().saldo
    if request.method == "POST":

        written_price = float(request.POST.get('price',''))
        written_desc= request.POST.get('desc','')
        selected_tipe = request.POST.get('tipeT', '')

        if selected_tipe == 'Credit':
            saldoCredit = written_price
            saldoDebit = 0
        elif selected_tipe == 'Debit':
            saldoDebit =  written_price
            saldoCredit =0
        else:
            return HttpResponse(400,'Salah input data')


        cf = cashFlow(price=written_price,desc=written_desc,saldoCredit=saldoCredit,tipe=selected_tipe,saldoDebit=saldoDebit)
        cf.save()
        return redirect('/')

    context={
      #  'cf_list':cf_list
    }
    return render(request,'finance/add.html',context)

def ubah(request,id):
    cfl = cashFlow.objects.get(id=id)
    form = cashflowForm(request.POST or None, instance=cfl)

    if form.is_valid():
        written_price = float(request.POST['price'])
        written_desc = request.POST['desc']
        selected_tipe = request.POST['tipe']

        if selected_tipe == 'Credit':
            saldoCredit = written_price
            saldoDebit = 0
            cf = cashFlow(price=written_price, desc=written_desc, saldoCredit=saldoCredit, tipe=selected_tipe,
                          saldoDebit=saldoDebit,id=id)
            cf.save()
            return redirect('/')

        elif selected_tipe == 'Debit':
            saldoDebit = written_price
            saldoCredit = 0
            cf = cashFlow(price=written_price, desc=written_desc, saldoCredit=saldoCredit, tipe=selected_tipe,
                          saldoDebit=saldoDebit,id=id)
            cf.save()
            return redirect('/')



    context = {
            'form': form, 'cf': cfl
    }
    return render(request, 'finance/ubah.html', context)

def hapus(request,id):
    cf = cashFlow.objects.get(id=id)
    if request.method =='POST':
        cf.delete()
        return redirect('/')

    context ={
        'cf':cf

    }
    return render(request,'finance/hapus.html',context)

def detail(request):

    cf_list = cashFlow.objects.all()
    cf_count = cf_list.count()

    myFilter = CashFlowFilter(request.GET, queryset=cf_list)
    cashflows = myFilter.qs

    context = {
        'cf_list': cf_list,'myFilter':myFilter,'cashflows':cashflows,'cf_count':cf_count
    }
    return render(request, 'finance/detail.html', context)


